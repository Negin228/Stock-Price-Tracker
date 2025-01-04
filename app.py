import psycopg2
import os
from flask import Flask, render_template, jsonify
import yfinance as yf

app = Flask(__name__)

# Database connection details (use environment variables for Heroku)
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def get_portfolio_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT symbol, name, price FROM portfolio')
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_stock_prices():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT symbol FROM portfolio')
    symbols = [row[0] for row in cursor.fetchall()]
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        try:
            price = stock.history(period='1d')['Close'][0]
            cursor.execute('UPDATE portfolio SET price = %s WHERE symbol = %s', (price, symbol))
        except IndexError:
            print(f"Failed to fetch data for {symbol}.")
    conn.commit()
    conn.close()
