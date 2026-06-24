from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

def generate_summary(news, stocks):

    formatted_news = "\n".join(
        [f"- {item['title']}" for item in news]
    )

    formatted_stocks = "\n".join(
        [f"{ticker}: ${price}"
         for ticker, price in stocks.items()]
    )

    prompt = f"""
You are my personal business assistant.

Business News:
{formatted_news}

Stock Prices:
{formatted_stocks}

Create:
1. Good morning greeting
2. Top news summary
3. Market summary
4. Key observations

Use simple English.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text