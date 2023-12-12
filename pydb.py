import sqlite3
db_name = 'quiz.sqlite'
conn = None
cursor = None
def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
def close():
    cursor.close()
    conn.close()
def do(query):
    cursor.execute(query)
    conn.commit()
