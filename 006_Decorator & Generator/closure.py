def outer_funtion(text):
    def inner_function():
        print(text)
    return inner_function()
my_func = outer_funtion("Hello World")

print('----------------------------------------')

def power(exponent):
    def power_of(base):
        return pow(base,exponent)
    return power_of
cube = power(3)
print(cube(2))
print(cube(3))


# Closures
# Wikipedia says, "A closure is a record storing a function together with
# an environment: a mapping associating each free variable of the function
# with the value or storage location to which the name was bound when the
# closure was created. A closure, unlike a plain function, allows the
# function to access those captured variables through the closure's
# reference to them, even when the function is invoked outside their
# scope."