import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('portfolio.db')
cursor = conn.cursor()

# Create table for stocks if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_symbol TEXT NOT NULL,
    stock_name TEXT
);
''')

# Commit and close
conn.commit()
conn.close()

print("Database setup complete.")
