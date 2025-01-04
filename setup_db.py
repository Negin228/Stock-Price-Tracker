import os
import psycopg2

# Get the database URL from the environment variable
DATABASE_URL = os.environ['DATABASE_URL']

# Connect to the database
conn = psycopg2.connect(DATABASE_URL)
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
cursor.execute('INSERT INTO portfolio (symbol, name, price) VALUES (%s, %s, %s) ON CONFLICT (symbol) DO NOTHING', ('AAPL', 'Apple Inc.', 150.00))
cursor.execute('INSERT INTO portfolio (symbol, name, price) VALUES (%s, %s, %s) ON CONFLICT (symbol) DO NOTHING', ('GOOGL', 'Alphabet Inc.', 2800.00))
cursor.execute('INSERT INTO portfolio (symbol, name, price) VALUES (%s, %s, %s) ON CONFLICT (symbol) DO NOTHING', ('MSFT', 'Microsoft Corp.', 300.00))
print("Sample data inserted")

# Commit changes and close connection
conn.commit()
conn.close()
print("Database connection closed")
