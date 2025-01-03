import sqlite3

def view_stocks():
    # Connect to SQLite database
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()

    # Query all stocks in the portfolio
    cursor.execute('SELECT id, stock_symbol, stock_name FROM stocks')
    stocks = cursor.fetchall()

    print("Stocks in your portfolio:")
    for stock in stocks:
        print(f"ID: {stock[0]}, Symbol: {stock[1]}, Name: {stock[2]}")

    conn.close()

view_stocks()
