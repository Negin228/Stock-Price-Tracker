from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_portfolio_data():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM portfolio')
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    portfolio = get_portfolio_data()
    return render_template('index.html', portfolio=portfolio)

if __name__ == '__main__':
    app.run(debug=True)
