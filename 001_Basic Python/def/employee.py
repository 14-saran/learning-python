#overloading
class Employee:
    #class variable
    __minSarary = 12000
    maxSalary = 50000
    companyName = "abc company.co"
    def __init__(self,name,salary,department): 
        #instance varible
        self.name = name
        self.salary = salary
        self.department = department
    #แสดงรายได้      
    def _showData(self):
        print("ชื่อพนง = "+self.name)
        print("เงินเดือน = ",format(self.salary))
        print("ตำแหน่ง = "+self.department)
    
    #รายได้ต่อปี
    def _getIncome(self):
        return self.salary *12
    
    def __str__(self):
        return "ชื่อพนักงาน = {}, แผนก = {}, เงินเดือน = {}, รายได้ต่อปี = {}".format(self.name, self.department, self.salary, self._getIncome())


class Accounting(Employee):
    departmentName = "แผนกบัญชี" 
    def __init__(self,name,salary,age):
        super().__init__(name, salary, Accounting.departmentName)
        self.age = age

    def _showData(self):
        super()._showData()
        print("อายุ = "+str(self.age))
        print("##############")


class Programmer(Employee):
    departmentName = "แผนกIT"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, Programmer.departmentName)
        self.exp = experience
        self.skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = "+str(self.exp))
        print("ทักษะ = "+self.skill)
        print("##############")

        
class Sale(Employee):
    departmentName = "แผนกขาย"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, Sale.departmentName)
        self.area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่ = "+self.area)
        print("##############")


account = Accounting("a",10000,32)
account._showData()
programmer = Programmer("b",20000,2,"python")
programmer._showData()
sale = Sale("c",30000,"เชียงใหม่")
programmer._showData()

