#Constructor in inh.
class A:

    def __init__(self):
        print("in A init") #ถ้าใน B ไม่มี จะเรีกในA ก่อน

    def feature1(self):
        print("Feature 1-A working")
    def feature2(self):
        print("Feature 2 working")

class B(A) : 
    def __init__(self):
        super().__init__()   #เข้าถึง คสบ.ทั้งหมดในmain class
        print("in B init") #ถ้าใน B มี > เรียก Bก่อน

    def feature1(self):
        print("Feature 1-B working")
    def feature4(self):
        print("Feature 4 working")

class C(B,A): 
    def __init__(self):
        super().__init__()
        print("in C init")
    
    def feat(self):
        super().feature2()

a1 = C()
a1.feature1()
a1.feat()