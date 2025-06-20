def add(x,y):
    return x+y
print(add(4,5))

add2 = lambda x,y: x+y
print(add2(4,5))

print('-----------------------------------------')

def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return(result)

nums = [1, 5,  6, 7, 8,]
cubde = my_map(lambda x: x**3 ,nums)
print(cubde)

print('-----------------------------------------')
# Lambda function = A small anonymous function for a bne time use (throw away function)
#                   They take any number of arguments, but have only 1 expression
#                   Helps keep the namespace clean and is useful with higher order functions
                    #'sort()', 'map()', 'filter()', 'reduce()'
                    #lambda parameters: expression
duble = lambda x: x**2
add = lambda x,y: x+y 
print(add(2,3))

duble = lambda x: x**2
add = lambda x,y: x+y 
max_value = lambda x,y: x if x>y else y
min_value = lambda x,y: x if x<y else y
print(max_value(8,5))
print(min_value(6,4))

full_name = lambda first, last : first + " " + last
is_even = lambda x: x%2 == 0
age_check = lambda age: True if age >= 18 else False
print(age_check(16)) 

print('-----------------------------------------')


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list (map (lambda x: x**2,my_numbers))
print (squares)

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8,9, 10]
evens = list (filter (lambda x: x % 2 == 0, my_numbers))
print (evens)

values = [(1, 'a', "hello"), (2,'a', "world"), (3,'c', "ok" )]
sorted_values = sorted (values, key = lambda x: x[1] + x[2])
print (list(sorted_values))

from functools import reduce
numbers = [1, 2, 3, 4, 5]
#3+3=6
#6+4=10
#10+5=15
# Using reduce to sum the list without initializer
sum_of_numbers = reduce(lambda acc, x: acc + x, numbers)
print(sum_of_numbers) 
# Using reduce to find the maximum value
max_value = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(max_value) 

