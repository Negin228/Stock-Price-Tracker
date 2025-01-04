import sqlite3

# Connect to SQLite
conn = sqlite3.connect('portfolio.db')  # This creates a file named portfolio.db in your app's directory
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS portfolio (
    symbol TEXT PRIMARY KEY,
    name TEXT,
    price REAL
)
''')
print("Table created successfully")

# Insert sample data
cursor.execute('INSERT OR IGNORE INTO portfolio (symbol, name, price) VALUES (?, ?, ?)', ('AAPL', 'Apple Inc.', 150.00))
cursor.execute('INSERT OR IGNORE INTO portfolio (symbol, name, price) VALUES (?, ?, ?)', ('GOOGL', 'Alphabet Inc.', 2800.00))
cursor.execute('INSERT OR IGNORE INTO portfolio (symbol, name, price) VALUES (?, ?, ?)', ('MSFT', 'Microsoft Corp.', 300.00))
print("Sample data inserted")

# Commit changes and close connection
conn.commit()
conn.close()
print("Database connection closed")
