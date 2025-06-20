#re.search
#match at any place unlike re.match
#does't need re.MULTILINE flag

import re

str1 = '''I am IP Guy
but python is good
'''
print(re.search(r'but' , str1).group())

#re.search('pattern', 'str')
#<re.Mach object; span=(0,2), match='py'
#                span เริ่มที่0หยุดที่2 ,matchกับ'py'ในstr ถ้าไม่ตรงจะได้ none

print('*-----------------------------------------')
#re.sub
#replace pattern in output string 


str2 = "I am IP Guy but python is good and IP is good too"
print(re.sub(r'IP', 'Network', str2, 1))

('**-----------------------------------------')

'''regular expression 
สร้าง แพทเทินการหา โดยข้อมูลที่จะเอาแพทเทินไปหาเป็นข้อมูล str '''
'''pattern
.at = มีอะไรก็ได้ที่ตำแหน่งจุดแล้วข้างหลังเป็นat
so* = หาพทที่มีso แล้วเกิดoซ๊ำ มีoตัวเดี่ยว หรือไม่มีก็ได้
so+ = จะต้องมีoอย่างน้อย1ตัวตรามหลังs
[Pp]y = ดึงข้อมูลทั้งPy&py
[a-zA-Z0-9-_]* = ตามด้วยอักษรอะไรก็ได้กี่ตัวก็ได้
'''


print('-----------------------------------------')

pattern = re.compile("^[a-zA-Z\s]+$")
print(pattern.search("Hello World"))
print(pattern.search("hello wrold"))
print(pattern.search("helloworld"))

print('-----------------------------------------')

#3 lowercase letters
#3-5 digits
# one symbol
# uoto two uppercase characters (optional)

pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")
print(pattern.search("ahk4567#CG"))
print(pattern.search("dll78944.L"))
print(pattern.search("dll78944."))
print(pattern.search("abc123456#JJ"))

print('-----------------------------------------')

pattern = re.compile("^.{10}S")
print(pattern.search("abcjdydsvx"))
print(pattern.search("0123456789"))
print(pattern.search("0.2#4J 789"))
print(pattern.search("abcdefghijk"))
print(pattern.search("abcdefghi"))

print('-----------------------------------------')

pattern = re.compile("^[a-zA-Z0-9.\-_]+@[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}$")
print(pattern.search("mail@neuralnine.com"))
print(pattern.search("mymail@test.travel"))
print(pattern.search("my_fancy.e-mail@fancyurl123.de"))
print(pattern.search("something.something.com"))
print(pattern.search("mail@something"))


