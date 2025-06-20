def add_items(*args, **kwargs):
    print(args ,kwargs)
    result = sum(args )
    print(result)

add_items(1, 2, 3, k=1, a=2)

print('-----------------------------------------')

def print_all(*args, **kwargs):
    print("Positonal:",args)
    print("keyword:", kwargs)

print_all(1,2,3, name="Aoi" , age=30)

print('-----------------------------------------')

#*args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#              * unpacking operator
#               1. positional 2. default 3. keyword 4. ARBITRARY

def add (*nums):
    total = 5
    for num in nums:
        total += num
    return total

print(add(1,2))

print('-----------------------------------------')

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    
display_name("dr . ","saran", "w")


print('-----------------------------------------')


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="123F",
              apt="100",
              city= "sala",
              state="MI",
              zip="73170")

print('-----------------------------------------')

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end= " ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}{kwargs.get('state')}{kwargs.get('zip')}")

shipping_label("dr . ","saran", "w",
               street="123F",
              pobox="PO box #100",
              city= "sala",
              state="MI",
              zip="10170")


