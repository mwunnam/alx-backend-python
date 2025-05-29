import time
import sqlite3 
import functools


query_cache = {}

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
       key = str((args, tuple(kwargs.items())))

       if key in query_cache:
           print("Returning cached result")
           return query_cache[key]
       
       try: 
           result = func(conn, *args, **kwargs)
           query_cache[key] = result
           return result
       except Exception as e:
           print(f"{e} error occured")
           raise
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(f" This is from the first call: {users}")
#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(f"This is from the second call: {users_again}")