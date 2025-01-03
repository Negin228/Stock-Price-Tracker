import yfinance as yf

def get_stock_prices(stock_symbols):
    stock_data = {}
    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        try:
            price = stock.history(period="1d")['Close'].iloc[-1]
            stock_data[symbol] = price
        except Exception as e:
            stock_data[symbol] = f"Error: {e}"
    return stock_data

def main():
    # Define the stock symbols you want to track
    stock_symbols = ["AAPL", "GOOG", "MSFT"]  # Replace with your stock symbols
    prices = get_stock_prices(stock_symbols)
    
    print("Latest Stock Prices:")
    for symbol, price in prices.items():
        print(f"{symbol}: {price}")

if __name__ == "__main__":
    main()

