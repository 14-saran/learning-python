
# csv_io.py
# อ่าน/เขียนไฟล์ .csv

import csv

# เขียนแบบลิสต์
with open("data.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["ชื่อ", "อายุ", "จังหวัด"])
    writer.writerow(["ส้ม", 25, "กรุงเทพฯ"])
    writer.writerow(["บอล", 30, "เชียงใหม่"])

# อ่านแบบลิสต์
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("ข้อมูลจากไฟล์ .csv (ลิสต์):")
    for row in reader:
        print(row)

# เขียนแบบ Dict
with open("data_dict.csv", "w", newline='', encoding="utf-8") as file:
    fieldnames = ["ชื่อ", "อายุ", "จังหวัด"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"ชื่อ": "ออม", "อายุ": 22, "จังหวัด": "ขอนแก่น"})

# อ่านแบบ Dict
with open("data_dict.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("ข้อมูลจากไฟล์ .csv (Dict):")
    for row in reader:
        print(row)
