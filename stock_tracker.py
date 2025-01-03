import sqlite3
import yfinance as yf

def fetch_stock_data():
    # Connect to SQLite database
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()

    # Get all stock symbols from the portfolio
    cursor.execute('SELECT stock_symbol FROM stocks')
    stock_symbols = cursor.fetchall()

    for symbol in stock_symbols:
        stock_symbol = symbol[0]
        stock_data = yf.Ticker(stock_symbol).history(period="1d")
        print(f"Stock: {stock_symbol}")
        print(stock_data.tail(1))  # Show latest data (e.g., last closing price)

    conn.close()

fetch_stock_data()
