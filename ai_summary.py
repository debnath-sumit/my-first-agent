from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

def generate_summary(news, stocks,emails):

    formatted_news = "\n".join(
        [f"- {item['title']}" for item in news]
    )

    formatted_stocks = "\n".join(
        [f"{ticker}: ${price}"
         for ticker, price in stocks.items()]
    )

    formatted_emails = "\n".join(
        [
            f"- From: {email['sender']}\n  Subject: {email['subject']}\n  Snippet: {email['snippet']}"
            for email in emails
        ]
    )

    prompt = f"""
    You are my personal executive assistant.

    Create a professional morning briefing.

    Use the following sections:

    # Good Morning Message

    # Business News
    Summarize the most important news.

    # Stock Market Snapshot
    Mention notable stock movements.

    # Important Emails
    Summarize key emails.

    # Action Items
    List actions I should take today.

    Keep it concise and professional.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text