import os
import numpy as np
import psycopg2
from flask import Flask
import yfinance as yf

app = Flask(__name__)

# Function to update stock prices in the database
def update_stock_prices():
    try:
        symbols = ['AAPL', 'GOOGL', 'AMZN']
        conn = psycopg2.connect(
            host=os.environ['DB_HOST'],
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD']
        )
        cursor = conn.cursor()

        for symbol in symbols:
            stock = yf.Ticker(symbol)
            price = stock.history(period='1d')['Close'][0]
            price = float(price)
            cursor.execute('UPDATE portfolio SET price = %s WHERE symbol = %s', (price, symbol))

        conn.commit()
    except Exception as e:
        print(f"Error updating stock prices: {e}")
    finally:
        cursor.close()
        conn.close()


@app.route('/refresh')
def refresh():
    update_stock_prices()
    return "Stock prices updated!"

if __name__ == "__main__":
    from os import environ
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))
