class Car:

    def __init__(self, make, model, year):
        self.make = make     
        self.model = model    
        self.year = year      

    def description(self):
        return f"{self.year} {self.make} {self.model}"

    def drive(self):
        return "go !"

class SUV(Car):

    def __init__(self, make, model, year, seating_capacity):
        super().__init__(make, model, year)
        self.seating_capacity = seating_capacity

    def description(self):
        return f"{super().description()} with seating capacity of {self.seating_capacity}"

    def drive(self):
        return "x10!"

car1 = Car("Ford", "Mustang", 2020)
print(car1.description()) 

suv1 = SUV("Toyota", "4Runner", 2022, 5)
print(suv1.description()) 
print(suv1.drive())
