#import aiosqlite
import asyncio
import os

DB_NAME = "users.db"

# Step 1: Set up database with some sample data
async def setup_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)  # Start fresh every time you run

    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)
        users = [
            ("Alice", 30),
            ("Bob", 45),
            ("Charlie", 25),
            ("Diana", 55),
            ("Eve", 41),
            ("Frank", 38)
        ]
        await db.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)
        await db.commit()