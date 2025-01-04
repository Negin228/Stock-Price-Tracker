import psycopg2
import os
from flask import Flask, render_template, jsonify
import yfinance as yf
import numpy as np

app = Flask(__name__)

# Function to update stock prices in the database
def update_stock_prices():
    # Replace with your stock symbols or other logic to fetch them
    symbols = ['AAPL', 'GOOGL', 'AMZN']  # Example stock symbols
    
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        host="your-database-host",
        database="your-database-name",
        user="your-username",
        password="your-password"
    )
    cursor = conn.cursor()
    
    for symbol in symbols:
        # Fetch the stock price using yfinance
        stock = yf.Ticker(symbol)
        price = stock.history(period='1d')['Close'][0]  # Get the latest closing price
        
        # Ensure price is a float and insert it into the database
        price = float(price)  # Ensure the price is a regular float type
        
        cursor.execute('UPDATE portfolio SET price = %s WHERE symbol = %s', (price, symbol))
    
    # Commit changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/refresh')
def refresh():
    update_stock_prices()
    return "Stock prices updated!"

if __name__ == "__main__":
    app.run(debug=True)
