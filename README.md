
# Learning Python
ดูตัวอย่าง code ได้ที่ [Github](https://github.com/14-saran/learning-python.git)

## Table of Contents
- [Python Basics](#python-basics)
- [Intermediate Functions](#intermediate-functions)
- [File I/O & Modules](#file-io--modules)
- [Error Handling & Testing](#error-handling--testing)
- [Strings & Regular Expressions](#strings--regular-expressions)
- [Decorators & Generators](#decorators--generators)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [SQLite & Web Scraping](#sqlite--web-scraping)
- [Concurrent Programming](#concurrent-programming)
- [DateTime & Python Tips](#datetime--python-tips)

---

## Python Basics

### Data Types
- `int` (จำนวนเต็ม) เช่น 5, -12, 1000  
- `float` (ทศนิยม) เช่น 3.14, -0.5, 2.0  
- `bool` (บูลีน) เช่น True, False  
- `str` (สตริง/ข้อความ) เช่น 'Hello', "World"

### Data Structures
- `list` เช่น [1, 2, 3], ['a', 'b']  
- `tuple` เช่น (1, 2, 3), ('x', 'y')  
- `set` เช่น {1, 2, 3}, {'a', 'b'}  
- `dict` เช่น {'name': 'Tom', 'age': 25}

### if / else
```python
if เงื่อนไข1:
    # คำสั่ง
elif เงื่อนไข2:
    # คำสั่ง
else:
    # คำสั่งถ้าไม่ตรงกับเงื่อนไขใดเลย
```

### Loop (for, while)
- `while` loop: ทำloop จากจุดเริ่ม-สิ้นสุด ต้องเป็นจริงถ้าไม่จะออกจากลูป 
- `for` loop: ใช้ไล่ลำดับในsetข้อมูลในloop

### def (Function)
- ใช้สร้างFunctionไว้ใช้เก็บชุดคำสั่งที่ สามารถเรียกใช้ซ้ำๆได้ 
```python
def ชื่อฟังก์ชัน(พารามิเตอร์):
    # คำสั่ง
    return ค่าที่ส่งกลับ  # ถ้ามี
```

---

## Intermediate Functions

### *args, **kwargs, Scope
- `*args`: เอาไว้ส่งข้อมูลหลายๆตัว แบบไม่ต้องบอกชื่อ  
- `**kwargs`: เอาไว้ส่งข้อมูลหลายๆตัว ที่มีชื่อกำกับ 
- Scope: ขอบเขตการเข้าถึงตัวแปรในฟังก์ชัน

### Lambda Function, Nested Function
- `Lambda`: ฟังก์ชันสั้นๆ ไม่มีการระบุชื่อ เขียนในบรรทัดเดียวจบ 
- `Nested Function`: ฟังก์ชันซ้อนฟังก์ชัน โดย functionข้างในสุด จะถูกคิดค่าก่อน แล้วใช้ค่านั้นเป็น args สำหรับfunctionถัดไปได้

### List Comprehension, Map, Filter, Zip, Enumerate
- `List Comprehension`: เป็นการสร้าง list  โดยวนลูป + ดัดแปลงข้อมูลได้สั้นๆบรรทัดเดียว
- `Map`: นำlist/objectที่วนซ้ำบางตัวได้บางตัวมาใช้ แล้วนำfunctionไปใช้กับค่านั้น  
- `Filter`: filterค่าในlist หรือ object ที่วนซ้ำได้บางประเภท แล้วส่งออกค่าที่เป็น True
- `Zip`:  เอาข้อมูล 2 ตัวขึ้นไป มาจับคู่กันแล้วเก็บในรูป tuple 
- `Enumerate`: เป็นfunctionที่ช่วยใส่ลำดับตัวเลขของข้อมูล เวลาใช้ loop 

---

## File I/O & Modules

### Read / Write: .txt, .csv, .json
- Read  : เอาข้อมูลจากไฟล์เข้าโปรแกรม
- Write : เอาข้อมูลไปเขียนลงไฟล์

- `.txt`: ข้อความธรรมดา  
- `.csv`: ข้อมูลตาราง (คอลัมน์-แถว)  
- `.json`: ข้อมูลโครงสร้าง (dict, list)

### โหมดไฟล์
| โหมด | ความหมาย | ใช้ทำอะไร |
|-------|---------|-----------|
| `'r'` | read    | อ่านไฟล์ (ถ้าไม่มีไฟล์จะ error) |
| `'w'` | write   | เขียนทับไฟล์ (ลบของเก่า) |
| `'a'` | append  | เขียนต่อท้ายไฟล์ (ถ้าไม่มีไฟล์จะสร้างใหม่) |

---

## Error Handling & Testing

### Try-Except, Finally
ใช้ตรวจสอบหาerror 
```python
try:
    # โค้ดที่อาจเกิด error
except SomeError:
    # ถ้าเกิด SomeError ทำอะไร
else:
    # ถ้าไม่ error ทำอะไร
finally:
    # ทำเสมอไม่ว่าจะ error หรือไม่
```

### Assert, Unittest Basics
- `Assert` : ใช้ทดสอบว่าcodeที่เขียนว่าเช็กTrueไหม
- `Unittest` : ใช้ทดสอบ class ว่าทำงานถูกไหม

---

## Strings & Regular Expressions
### String Methods, Formatting
\* ตัวอย่าง code ในไฟล์ str.py *
- isalpha() : เช็คว่าเป็นอักษรEn ทั้งหมดหรือไม่
- isdigit() : เป็นตัวเลขจำนวนเต็มหรือไม่
- find() : เช็คsrt ว่าเจอครั้งแรกที่indexไหน
- lowwer,upper : เปลี่ยนเป็นตัวพิมพ์เล็ก,ใหญ่ทั้งหมด
- strip() : ตัดเว้นวรรคข้างหน้าและข้างหลังออกทั้งหมด
- replace() : แทนที่ข้อความ
- split() : แบ่งlist จากช่องว่าง
- join() : นำ something ไป join ร่วมกับ str
- capitalize : ทำตัวแรกให้เป็นตัวพิมพ์ใหญ่
- title : เปลียนคำขึ้นต้นทุกตัวให้เป็นตัวพิมพ์ใหญ่
- format() : นำข้อมูลไปลง {}

### re.search, re.sub, Pattern Matching
- `re.search`('pattern', 'str')  
ใช้patternหาข้อความ ถ้าเจอ pattern ตรงกัน ตรงไหนก็ได้ ถือว่า match  
```python
import re

str1 = '''I am IP Guy
but python is good
'''
print(re.search(r'but' , str1).group())
```
output คือ re.Mach object; span=(0,2), match='py'  
        > span เริ่มที่0หยุดที่2   
        > matchกับ'py'ในstr ถ้าไม่ตรงจะได้ none

- `re.sub` หา pattern ที่ match แล้วแทนที่ด้วยคำใหม่
```python
str2 = "I am IP Guy but python is good and IP is good too"
print(re.sub(r'IP', 'Network', str2, 1))
```
---

## Decorators & Generators

### Nested Functions and Closures
- `nested function` : คือ functonประกาศอยู่ข้างในอีกฟังก์ชันหนึ่ง"
```python
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()
```

- `Closures` : คือ functionที่จำค่า ตัวแปรข้างนอกได้ แม้ว่าฟังก์ชันนั้นจะถูกเรียกใช้แล้ว  
(functionข้างใน ถูกreturnออกไปแล้ว แต่ยังจำค่าเก่าได้)
```python
def power(exponent):
    def power_of(base):
        return pow(base,exponent)
    return power_of
cube = power(3)
print(cube(2))
print(cube(3))
#power_of คือ ฟังก์ชันข้างใน
```

### Decorators Basics and Applications
-

### Generator Functions with Yield
- 

---

## Object-Oriented Programming (OOP)

### Class, __init__, Method, Attributes
-

### Inheritance, Polymorphism, super()
-

---

## SQLite & Web Scraping

### Working with sqlite3
-

### Web Scraping Using BeautifulSoup
-

---

## Concurrent Programming

### Multithreading


### Multiprocessing and Async Basics


---

## DateTime & Python Tips

### datetime, timedelta, strftime


### Python Tricks: Unpacking, Ternary, F-String, Walrus

