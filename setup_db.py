import sqlite3

# Connect to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('portfolio.db')
cursor = conn.cursor()

# Create the 'portfolio' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS portfolio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT UNIQUE,
    name TEXT
);
''')

# Commit changes and close the connection
conn.commit()
conn.close()
