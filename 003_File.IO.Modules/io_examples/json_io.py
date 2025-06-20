
# json_io.py
# อ่าน/เขียนไฟล์ .json

import json

# ข้อมูลตัวอย่าง
data = {
    "name": "นัท",
    "age": 26,
    "skills": ["Python", "Odoo", "SQL"]
}

# เขียนไฟล์ .json
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# อ่านไฟล์ .json
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print("ข้อมูลจากไฟล์ .json:")
    print(data)
    print("ชื่อ:", data["name"])
