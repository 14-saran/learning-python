# ----------------------------
# Method Overloading
# ----------------------------

def create_invoice(customer=None, amount=None, tax=None):
    # customer = ชื่อลูกค้า
    # amount = จำนวนเงินก่อนภาษี
    # tax = อัตราภาษี %

    if customer is None and amount is None:
        print("Error: Missing invoice data")
    elif tax is None:
        print(f"Invoice for {customer} | Amount: {amount} (No Tax Applied)")
    else:
        total = amount + (amount * tax / 100)
        print(f"Invoice for {customer} | Amount: {amount} | Tax: {tax}% | Total: {total}")

create_invoice()
create_invoice("บริษัท A", 10000)
create_invoice("บริษัท B", 20000, 7)

print("------------------------------------------")

# ----------------------------
# Method Overriding
# ----------------------------

class Account:
    def report(self):
        print("Generating General Account Report")

class CustomerAccount(Account):
    def report(self):
        print("Generating Customer Account Report with Outstanding Balances")

c1 = CustomerAccount()
c1.report()

a = Account()
a.report()

print("------------------------------------------")

# ----------------------------
# Operator Overloading
# ----------------------------

class Invoice:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, other_invoice):
        return Invoice(self.amount + other_invoice.amount)
    
    def __str__(self):
        return f"Invoice Amount: {self.amount}"

inv1 = Invoice(15000)
inv2 = Invoice(20000)

print(inv1)
print(inv2)

# รวมยอด invoice ทั้ง 2 ใบ
inv_total = inv1 + inv2
print(inv_total)
