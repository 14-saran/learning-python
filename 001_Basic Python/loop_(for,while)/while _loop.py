#while loop = excute some code WHILE  condiyion remains true

name = input("Enter your name: ")

while name == "": #เรียกว่า ลูปไม่สิ้นสุด
    print("you did not enter your name")
    name = input("Enter your name: ")
else:
    print(f"hello {name}")

print('-----------------------------------------')

age = int(input("Enter your age: "))

while age <0 : 
    print("Age can't be negative!")
    age = int(input("Enter your age: "))
print(f"you are {age} years old")
