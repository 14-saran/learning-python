import tkinter as tk
from tkinter import ttk

import DBconnect as db

def add_data():
    name = name_entry.get() # type: ignore
    age = int(age_entry.get()) # type: ignore

    db.insertfunc(name, age)

    name_entry.delete(0, tk.END) # type: ignore
    age_entry.delete(0, tk.END) # type: ignore

    show_data()


def delete_data():
    select_item = tree.selection() # type: ignore

    for item in select_item:
        rec_id = tree.item(item, "values")[0] # type: ignore
        print(rec_id)
        db.deletefunc(rec_id)

    show_data()


def show_data():
    # ลบข้อมูลเก่า
    for row in tree.get_children(): # type: ignore
        tree.delete(row) # type: ignore

    rows = db.get_data()

    for i in rows:
        tree.insert('', tk.END, values=i) # type: ignore
