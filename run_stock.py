from stock_tool import get_stock_prices

stocks = get_stock_prices(
    ["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"]
)

print(stocks)