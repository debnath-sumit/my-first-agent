from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from news_tool import get_business_news
from stock_tool import get_stock_prices
from gmail_tool import get_top_emails
from weather_tool import get_weather

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


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

tools = [
    business_news_tool,
    stock_price_tool,
    gmail_tool,
    weather_tool
]

agent = create_react_agent(
    llm,
    tools
)


def run_agent(user_request: str):
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