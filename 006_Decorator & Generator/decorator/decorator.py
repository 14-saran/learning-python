# Decorator

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*you add sprinkles*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("'*you add fudge*'")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_ice_cream("matcha")

print('---------------------------------------------')

class Person:
    species = "Homo sapiens"

    @classmethod
    def get_species(cls):
        print(cls)
        return cls.species
# Usage
print(Person.get_species()) 

def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    return wrapper
@f1
def f(a):
    print(a)

f("hello")


print("----------------------------------------")


def f2(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val =  func(*args, **kwargs)
        print("Ended")
        return val
    
    return wrapper

@f2
def c(a, b=9):
    print(a, b)

@f2
def add(x,y):
    return x + y

print(add(4, 5))
    


'''
def my_decorator(func):
    def wrapper():
        print("ก่อนเรียกฟังก์ชัน")
        func()
        print("หลังเรียกฟังก์ชัน")
    return wrapper

@my_decorator
def say_hello():
    print("Hello World!")

say_hello() '''

