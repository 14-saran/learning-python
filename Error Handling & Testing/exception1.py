# exception = An event that interrupts the flow of a program
#           (ZeroDivisionError, TypeError, ValueError)
#           1.try 2.except, 3.finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError: #	หารด้วยศูนย์
    print("you can't divide by Zero IDIOT!")
except ValueError: # ค่าที่รับมาไม่ถูกต้อง
    print("Enter only numbers please!")
except Exception: #จับ error หมดทุกชนิด
    print("Something went wrong!")
finally: 
    print("Do some cleanup here")