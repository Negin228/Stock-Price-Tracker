import sqlite3

# Connect to the portfolio database
conn = sqlite3.connect('portfolio.db')
cursor = conn.cursor()

# Function to add a stock to the portfolio database
def add_stock_to_portfolio(symbol, name):
    cursor.execute('''
        INSERT INTO portfolio (symbol, name) 
        VALUES (?, ?) 
        ON CONFLICT(symbol) DO NOTHING;
    ''', (symbol, name))
    conn.commit()

# Add predefined stocks to the portfolio
def add_predefined_stocks():
    stocks = ['AAPL', 'GOOG', 'AMZN']  # List of stock symbols you want to track
    for symbol in stocks:
        add_stock_to_portfolio(symbol, name=symbol)  # Add each stock to the portfolio

# Call the function to add predefined stocks
add_predefined_stocks()

# Close the database connection
conn.close()
