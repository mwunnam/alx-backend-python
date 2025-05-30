import sqlite3
import aiosqlite
import asyncio

async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            async for row in cursor:
                print(row)

async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            async for row in cursor:
                print(row)


async def fetch_concurrently():
    result  = await asyncio.gather(
        async_fetch_users(), 
        async_fetch_older_users()
    )
    return result

asyncio.run(fetch_concurrently())