import yfinance as yf

def get_stock_prices(symbols):

    prices = {}

    for symbol in symbols:
        ticker = yf.Ticker(symbol)

        data = ticker.history(period="1d")

        if not data.empty:
            prices[symbol] = round(
                data["Close"].iloc[-1], 2
            )

    return prices