import tkinter as tk
from tkinter import ttk
import sqlite3

import DBconnect as db

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()



def add_data():'''
    name = name_entry.get()
    age = age_entry.get()

    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)'''



def delete_data():
    select_item = tree.selection()

    for item in select_item:
        rec_id = tree.item(item, "values")
        print(rec_id[0])

    cursor.execute('DELETE FROM users WHERE id=' + rec_id[0])
    conn.commit()

    show_data()

        

def show_data():

    # ลบข้อมูลเก่า
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for i in rows:
        tree.insert('', tk.END, values=i)



# ----- GUI -----
root = tk.Tk()
root.title('Python GUI')

form_frame = ttk.Frame(root, padding=(20, 10))
form_frame.pack()

# ฟอร์มกรอกข้อมูล
name_label = ttk.Label(form_frame, text='ชื่อ :', font=(16))
name_label.grid(row=0, column=0, sticky='w')
name_entry = ttk.Entry(form_frame ,width= 35)
name_entry.grid(row=0, column=1, columnspan=2)

age_label = ttk.Label(form_frame,text='อายุ :',font=(16))
age_label.grid(row=1, column=0, sticky='w')
age_entry = ttk.Entry(form_frame, width= 35)
age_entry.grid(row=1, column=1, columnspan=2)

# ปุ่ม
add_button = ttk.Button(form_frame, text='เพิ่มข้อมูล', width=20, command=add_data)
add_button.grid(row=2, column=0, columnspan=2, pady=20)

delete_button = ttk.Button(form_frame, text='ลบข้อมูล', width=20, command=delete_data)
delete_button.grid(row=2, column=2, columnspan=2, pady=20)

# แสดงรายการข้อมูล
tree_frame = ttk.Frame(root)
tree_frame.pack(pady=10)

tree = ttk.Treeview(tree_frame, columns=('ID', 'name', 'age'), show='headings')
tree.heading('ID', text='ID')
tree.heading('name', text='ชื่อ')
tree.heading('age', text='อายุ')
tree.pack()

show_data()

root.mainloop()
