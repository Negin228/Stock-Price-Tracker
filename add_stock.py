import sqlite3
import yfinance as yf

# Connect to the portfolio database
conn = sqlite3.connect('portfolio.db')
cursor = conn.cursor()

# Create the portfolio table if it does not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS portfolio (
        symbol TEXT PRIMARY KEY,
        name TEXT,
        price REAL
    );
''')

# Function to get stock price using yfinance
def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    price = stock.history(period='1d')['Close'][0]
    return price

# Function to add a stock to the portfolio database
def add_stock_to_portfolio(symbol, name, price):
    cursor.execute('''
        INSERT INTO portfolio (symbol, name, price) 
        VALUES (?, ?, ?) 
        ON CONFLICT(symbol) DO NOTHING;
    ''', (symbol, name, price))
    conn.commit()

# Add predefined stocks to the portfolio
def add_predefined_stocks():
    stocks = ['AAPL', 'GOOG', 'AMZN']  # List of stock symbols you want to track
    for symbol in stocks:
        price = get_stock_price(symbol)
        add_stock_to_portfolio(symbol, name=symbol, price=price)  # Add each stock to the portfolio

# Call the function to add predefined stocks
add_predefined_stocks()

# Print the contents of the portfolio table
cursor.execute('SELECT * FROM portfolio')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the database connection
conn.close()
