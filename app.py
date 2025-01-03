from flask import Flask, render_template, jsonify
import sqlite3
import yfinance as yf

app = Flask(__name__)

def get_portfolio_data():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM portfolio')
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_stock_prices():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('SELECT symbol FROM portfolio')
    symbols = [row[0] for row in cursor.fetchall()]
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        price = stock.history(period='1d')['Close'][0]
        cursor.execute('UPDATE portfolio SET price = ? WHERE symbol = ?', (price, symbol))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    portfolio = get_portfolio_data()
    return render_template('index.html', portfolio=portfolio)

@app.route('/refresh')
def refresh():
    update_stock_prices()
    portfolio = get_portfolio_data()
    return jsonify([{'symbol': stock[0], 'name': stock[1], 'price': stock[2]} for stock in portfolio])

if __name__ == '__main__':
    app.run(debug=True)
