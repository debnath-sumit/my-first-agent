from news_tool import get_business_news
from stock_tool import get_stock_prices
from ai_summary import generate_summary

news = get_business_news()

stocks = get_stock_prices(
    ["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"]
)

summary = generate_summary(news, stocks)

print(summary)