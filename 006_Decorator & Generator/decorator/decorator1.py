from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity
    
p1 = Product(name="Laptop", price=1000.0, quantity=3)
p2 = Product(name="Laptop", price=1000.0, quantity=3)
p3 = Product(name="Smartphone", price=500.0, quantity=2)

print(p1.total_cost())