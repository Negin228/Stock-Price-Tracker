import os
import numpy as np
import psycopg2
from flask import Flask, render_template
import yfinance as yf

# Check if DB_HOST is set
db_host = os.environ.get('DB_HOST')
if db_host is None:
    print("DB_HOST is not set")

app = Flask(__name__)

# Function to update stock prices in the database
def update_stock_prices():
    symbols = ['AAPL', 'GOOGL', 'AMZN']  # Example stock symbols
    
    # Connect to your PostgreSQL database using environment variables
    conn = psycopg2.connect(
        host=db_host,
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    cursor = conn.cursor()
    
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        price = stock.history(period='1d')['Close'][0]  # Get the latest closing price
        
        price = float(price)  # Ensure the price is a regular float type
        
        cursor.execute('UPDATE portfolio SET price = %s WHERE symbol = %s', (price, symbol))
    
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')  # Ensure that index.html is in the 'templates' folder

@app.route('/refresh')
def refresh():
    update_stock_prices()
    return "Stock prices updated!"

if __name__ == "__main__":
    from os import environ
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))
