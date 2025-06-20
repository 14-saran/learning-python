#Inheritance
#self.name สืบทอดคสบ.จาก functionด้านบน def __init__(self.name,color)

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A) : #สามารถใช้feature ได้ทั้งในA&B (1-4)  ; A = super class ,B=sub class
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B):  #multi level inh.  #สามารถใช้feature ได้ทั้งในA,B&C
    def feature5(self):
        print("Feature 5 working")

    def feature2(self):
        print("Feature 2 working")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
c1 = C()


