
# ------------------------------
# หัวข้อ: *args, **kwargs และ Scope ใน Python
# ------------------------------

# -----------------------------------
# PART 1: *args (รับค่าหลายตัวแบบไม่ระบุจำนวน)
# -----------------------------------

def demo_args(*args):
    print("Received args:", args)
    for item in args:
        print("Item:", item)

# ทดลองเรียกใช้
demo_args(10, 20, 30)

# -----------------------------------
# PART 2: **kwargs (รับค่าแบบ key=value หลายตัว)
# -----------------------------------

def demo_kwargs(**kwargs):
    print("Received kwargs:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# ทดลองเรียกใช้
demo_kwargs(name="Alice", age=25)

# -----------------------------------
# PART 3: ใช้ *args และ **kwargs ร่วมกัน
# -----------------------------------

def mixed_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

mixed_args_kwargs(1, 2, x=3, y=4)

# -----------------------------------
# PART 4: Scope (ขอบเขตตัวแปร)
# -----------------------------------

# 1. Local Scope (ใช้ได้เฉพาะในฟังก์ชัน)
def local_scope():
    x = "local"
    print("Inside function:", x)

local_scope()
# print(x)  # ❌ จะ error เพราะ x เป็น local

# 2. Global Scope (ใช้ได้ทั่วไฟล์)
y = "global"

def global_scope():
    print("Inside function (global):", y)

global_scope()
print("Outside function:", y)

# 3. ใช้ global keyword เพื่อแก้ค่าจากในฟังก์ชัน
z = 10

def modify_global():
    global z
    z += 5

modify_global()
print("z after modify:", z)

# 4. ใช้ nonlocal ในฟังก์ชันซ้อน
def outer_func():
    message = "Hi"

    def inner_func():
        nonlocal message
        message = "Hello"

    inner_func()
    print("Message after inner call:", message)

outer_func()



print('-----------------------------------------')
# -----------------------------------
# แบบฝึกหัดท้ายบท (ลองทำดู)
# -----------------------------------

# 1. สร้างฟังก์ชันรับ *args แล้วคืนผลรวม
def sum_args(*args):
    result = sum(args)
    print(result)

sum_args(88,45,14)

# 2. สร้างฟังก์ชันรับ **kwargs แล้วคืน key ที่มีค่าเป็นเลขจำนวนเต็ม
def numeric_keys(**kwargs):
    result = []
    for key, value in kwargs.items():
         if isinstance(value, int):
            result.append(key)
    return result

output = numeric_keys(a=12.45, b=45, c=10, d="abc")
print(output)

# 3. ใช้ global เพื่อเปลี่ยนค่าตัวแปรจากในฟังก์ชัน
counter = 0
def modify_counter():
    global counter
    counter += 5 
    
modify_counter() 
print("Outside after modify:",counter )

# 4. ใช้ nonlocal เพื่อเปลี่ยนค่าตัวแปรของฟังก์ชันแม่
def change_message():
    msg = "start"

    def updater():
        nonlocal msg
        msg = "end"

    updater()
    print("Updated message:", msg)
change_message()
