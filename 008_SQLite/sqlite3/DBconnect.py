# เชื่อมต่อฐานข้อมูล
import sqlite3


def connect_db(): #เชื่อมฐานข้อมูล
    conn = sqlite3.connect('mydatabase.db')
    return conn


def get_data(): #เรียกดูข้อมูล
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    return rows

def insertfunc(name, age):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO users (name, age) VALUES (?,?)', (name ,age))
    conn.commit()
    conn.close ( )

def deletefunc(id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id="+ id)
    conn.commit()


def updatefunc(id, name, age):
    pass
