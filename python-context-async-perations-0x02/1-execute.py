import sqlite3

class ExecuteQuery():
    def __init__(self, db_name, query, params=None, ):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.conn = None
        self.curson = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        result = self.cursor.fetchall()
        return result 

    
    def __exit__(self, type, value, traceback):
        if self.conn:
            self.conn.close()



query = "SELCT * FROM users WHERE age > ?"
params = (25, )

with ExecuteQuery("users.db", query, params) as results:
    for row in results:
        print(row)