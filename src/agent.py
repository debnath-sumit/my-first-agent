import re

from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from src.tools.news_tool import get_business_news
from src.tools.stock_tool import get_stock_prices
from src.tools.gmail_tool import get_top_emails
from src.tools.weather_tool import get_weather
from src.llm.llm_factory import get_llm
from src.memory.pinecone_store import (
    search_memory,
    save_memory,
    format_memory_results
)

load_dotenv()


@tool
def business_news_tool() -> str:
    """Get top business news."""
    news = get_business_news()
    return str(news)


@tool
def stock_price_tool() -> str:
    """Get stock prices for AAPL, MSFT, GOOGL, NVDA, and TSLA."""
    stocks = get_stock_prices(["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"])
    return str(stocks)


@tool
def gmail_tool() -> str:
    """Get top recent Gmail emails."""
    emails = get_top_emails()
    return str(emails)


@tool
def weather_tool(city: str) -> str:
    """Get current weather for a city."""
    weather = get_weather(city)
    return str(weather)

@tool
def search_memory_tool(query: str) -> str:
    """Search previous saved memories. Input should be a simple text query."""
    results = search_memory(query)
    return format_memory_results(results)

@tool
def save_memory_tool(memory_text: str) -> str:
    """
    Save an important user-provided memory to Pinecone.
    Use this when the user says remember, save this, store this, note this, or keep this in memory.
    """
    return save_memory(memory_text, memory_type="user_profile")



tools = [
    business_news_tool,
    stock_price_tool,
    gmail_tool,
    weather_tool,
    search_memory_tool,
    save_memory_tool
]

def create_agent(model_name):
    llm = get_llm(model_name)
    return create_react_agent(llm, tools)

memory_keywords = [
    "remember",
    "memory",
    "my name",
    "who am i",
    "about me",
    "recall",
    "previous",
    "yesterday",
    "last time",
]

def run_agent(user_request, model_name):
    stripped = user_request.strip()
    lower_request = stripped.lower()

    # Matches "remember this: X", "Remember this : X", "remember: X", etc.
    remember_match = re.match(
        r"^remember(?:\s+this)?\s*:\s*(.+)$",
        stripped,
        re.IGNORECASE | re.DOTALL,
    )
    if remember_match:
        memory_text = remember_match.group(1).strip()
        save_memory(memory_text, memory_type="user_profile")
        return f"Saved to memory: {memory_text}"

    if "my name is" in lower_request and "remember" in lower_request:
        save_memory(user_request, memory_type="user_profile")
        return "Saved to memory."

    if (
        "what is my name" in lower_request
        or "do you remember my name" in lower_request
        or "who am i" in lower_request
        or "what do you remember about me" in lower_request
    ):
        results = search_memory(user_request, memory_type="user_profile")
        return format_memory_results(results)

    agent = create_agent(model_name)

    result = agent.invoke(
        {
            "messages": [
                ("user", user_request)
            ]
        }
    )

    final_message = result["messages"][-1]

    if isinstance(final_message.content, list):
        return final_message.content[0]["text"]

    return final_message.content