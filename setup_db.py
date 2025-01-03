import sqlite3

# Database file
DB_FILE = "portfolio.db"

def create_table():
    """Create the portfolio table if it doesn't exist."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS portfolio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT UNIQUE NOT NULL
        )
        """)
        conn.commit()
        print("Table 'portfolio' has been created (if it didn't exist already).")

if __name__ == "__main__":
    create_table()
