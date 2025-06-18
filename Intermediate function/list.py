# list comprehension = A conciese way to create listr in python
#                       Compact and essier to read than traditional loops
#                       [expression for value in interable if condition]

double = [x * 2 for x in range(1, 11)]
triple = [y * 3 for y in range(1, 11)]
squares = [z * 2 for z in range(1, 11)]
print(squares)

print('-----------------------------------------')

fruits = ['apple', 'banana', 'coconut', 'giwi']
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)

print('-----------------------------------------')

numbers = [1, -2 , 3,-4, 5, -6, 8]
positive_nums = [num for num in numbers if num >= 0 ]
negative_nums = [num for num in numbers if num < 0 ]
even_nums = [num for num in numbers if num % 2 == 0]
oddo_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(oddo_nums)

print('-----------------------------------------')

grades = [85, 42, 79, 90, 56, 61]
passing_grade = [grade for grade in grades if grade >= 60]
print(passing_grade)
