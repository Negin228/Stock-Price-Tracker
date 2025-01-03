import sqlite3

# Connect to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('portfolio.db')
cursor = conn.cursor()

# Create the 'stocks' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_symbol TEXT UNIQUE,
    stock_name TEXT
);
''')

# Commit changes and close the connection
conn.commit()
conn.close()
