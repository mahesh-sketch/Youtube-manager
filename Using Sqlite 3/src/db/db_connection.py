import sqlite3

def dbConnection(dbname):
    try:
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
            )
            ''')
        print("Db Connected Successfully")
        return conn,cursor
    except Exception as e:
        print("Something went wrong !",e)
        return None,None