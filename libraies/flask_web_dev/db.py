import sqlite3

# Connect to SQLite DB (will create 'user_db.sqlite' if it doesn't exist)
conn = sqlite3.connect('user_db.sqlite')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create 'users' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and 'users' table created successfully.")