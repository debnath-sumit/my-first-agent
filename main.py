from news_tool import get_business_news
from stock_tool import get_stock_prices
from gmail_tool import get_top_emails
from ai_summary import generate_summary
from datetime import datetime


def run_morning_brief():
    print("Starting My First Agent...\n")

    print("Fetching business news...")
    news = get_business_news()

    print("Fetching stock prices...")
    stocks = get_stock_prices(
        ["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"]
    )

    print("Fetching Gmail emails...")
    emails = get_top_emails()

    print("Generating AI summary...\n")
    summary = generate_summary(news, stocks, emails)

    print("=" * 50)
    print("SUMIT'S MORNING BRIEF")
    print("=" * 50)
    print(summary)
    print(type(summary))
    today = datetime.today().strftime("%Y-%m-%d")
    file_name = f"morning_brief_{today}.txt"
    with open(file_name, "w") as file:
        file.write(summary)


if __name__ == "__main__":
    run_morning_brief()