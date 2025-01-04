import sqlite3

# Connect to the database
conn = sqlite3.connect('portfolio.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS portfolio (
    symbol TEXT PRIMARY KEY,
    name TEXT,
    price REAL
)
''')

# Insert sample data
cursor.execute('INSERT OR IGNORE INTO portfolio (symbol, name, price) VALUES (?, ?, ?)', ('AAPL', 'Apple Inc.', 150.00))
cursor.execute('INSERT OR IGNORE INTO portfolio (symbol, name, price) VALUES (?, ?, ?)', ('GOOGL', 'Alphabet Inc.', 2800.00))
cursor.execute('INSERT OR IGNORE INTO portfolio (symbol, name, price) VALUES (?, ?, ?)', ('MSFT', 'Microsoft Corp.', 300.00))

# Commit changes and close connection
conn.commit()
conn.close()
