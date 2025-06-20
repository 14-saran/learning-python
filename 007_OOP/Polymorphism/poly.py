# Method Overloading
def worker(x=None, y=None, z=None):
    #x = no of hours
    #z = bonus
    if x==None and z==None:
        print("sad")
    elif x <= 10 and z=="Yes":
        print("Dancing Worker")
    elif x <= 10 and z=="No":
        print("No working Strik...!")
    else:
        print ("Too much work hire someone")

worker()
worker(5,"Yes")


print("------------------------------------------")


## Method Overriding
class gaji:
    def property(self):
        print("I have 4CR property")
class child(gaji):
    def property(self):
        print("I have 40CR")

c1 = child()
c1.property()

g = gaji()
g.property()

print("------------------------------------------")


## Operator Overloading
3+5
"MAMA"+ "MOOSUB"

class price:
    def __init__(self, x):
        self.x = x
    
    def __add__(self, obj2):
        return self.x + obj2.x

obj1 = price(10)
obj2 = price(18)

print(obj1.x)  
print(obj2.x)

print(obj1 + obj2)

















