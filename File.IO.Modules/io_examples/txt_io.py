
# txt_io.py
# อ่าน/เขียนไฟล์ .txt

# เขียนไฟล์ .txt
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("สวัสดีครับ\n")
    file.write("นี่คือไฟล์ตัวอย่าง\n")

# อ่านไฟล์ .txt
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("เนื้อหาไฟล์ .txt:")
    print(content)

# อ่านทีละบรรทัด
with open("example.txt", "r", encoding="utf-8") as file:
    print("อ่านทีละบรรทัด:")
    for line in file:
        print(line.strip())
