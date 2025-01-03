import sqlite3

def add_stock_to_portfolio(symbol, name=None):
    # Connect to SQLite database
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()

    # Insert the stock symbol and name into the database
    cursor.execute('''
    INSERT INTO stocks (stock_symbol, stock_name)
    VALUES (?, ?)
    ''', (symbol, name))

    # Commit and close
    conn.commit()
    conn.close()
    
    print(f"Added {symbol} to the portfolio.")

# Example usage:
stock_symbol = input("Enter the stock symbol: ")
stock_name = input("Enter the stock name (optional): ")
add_stock_to_portfolio(stock_symbol, stock_name)
