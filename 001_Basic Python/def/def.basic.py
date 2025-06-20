# function = A block of reusable code
#           place() after the function  name to invoke

def happy_birthday(x, y):
    print(f"Happy birthday to {x}!")
    print(f"You are {y} years old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Bro",12)
happy_birthday ("Beab",45) 
happy_birthday ("Bob",41)


'-----------------------------------------'
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("PchaiJel", 30 ,"14/07")

# return = statement used to end a function
#   and send a result back to the caller

def create_name (first, last):
    first = first. capitalize()
    last = last. capitalize()
    return first + " " + last

full_name = create_name ("saran", "w")
print (full_name)