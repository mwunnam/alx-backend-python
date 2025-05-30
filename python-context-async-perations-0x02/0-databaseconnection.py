import sqlite3

class DatabaseConnection(object):
    def __init__(self, query, db_name):
        self.query = query
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query)
        return self.cursor.fetchall()

    def __exit__(self, type, value, traceback):
        if self.conn:
            self.conn.close()

select_table = "SELECT * FROM users"
with DatabaseConnection(select_table, "users.db") as f:
    for x in f:
        print(x)