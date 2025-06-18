names= ["Tom", "Jerry", "Alice"]
ages = [20, 25, 30]

for name, age in zip(names, ages):
    print(name, age)

for i, name in enumerate(names):
    print(name , i)

print('-----------------------------------------')

x = [1,2,3,4]
y = [1,1,3,7,9]

print(list(zip(y,x)))


print('-----------------------------------------')

# zip(+iterables) = aggregate elements from two or more iterables (Ifist, tuples, sets, etc.)
#                      creates a zip object with paired elements stored in tuples for each elemer

usernames = ["a", "b", "c"]
password = ("1234", "abcd", "456")
login_date = ["1/1/2025","2/2/2025","3/3/2025"]

users = zip(usernames,password,login_date)

for i in users:
    print(i)

print('-----------------------------------------')

#enumerate
shopping_list = ['apple', 'oranges', 'better', 'eggs']

for index,item in enumerate(shopping_list, 1):
    print("Item{0} : {1}".format(index, item))