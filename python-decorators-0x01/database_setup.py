import sqlite3

# Connect to / create the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the user Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
""")

sample_users = [
    ('Alice Johnson', 'alice@example.com'),
    ('Bob Smith', 'bob@example.com'),
    ('Charlie Brown', 'charlie@example.com')
]

cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', sample_users)

conn.commit()
conn.close()

print("✅ Database 'users.db' created with table 'users' and sample data.")