#SQLite
import sqlite3

#เชื่อมต่อฐานข้อมูล
conn = sqlite3.connect('mydatabase.db')
#สร้างคำสั่งรันSQL
cursor = conn.cursor()

# สร้างตาราง
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER )''')
'''
#แทรกข้อมูลลงในตาราง
cursor.execute("insert INTO users (name,age) VALUES (?,?)",('Alice',25))
conn.commit()   # บันทึกการเปลี่ยนแปลง


data = [
    ('Bob', 15), 
    ('Charlie', 7), 
    ('David', 30), 
    ('Eve', 12)
]
cursor.executemany("INSERT INTO users (name, age) VALUES (?,?)", data)
conn.commit()'''  # บันทึกการเปลี่ยนแปลง 


# การเรียกดูข้อมูลในตาราง
cursor.execute('SELECT name , age FROM users')
rows = cursor.fetchall()

for i in rows:
    print(i[0] + ' ' + str(i[1]))

# แก้ไขข้อมูล
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (28, 'Alice'))
conn.commit()

# แก้ไขข้อมูล
cursor.execute("DELETE FROM users WHERE name = 'Bob")
conn.commit()



