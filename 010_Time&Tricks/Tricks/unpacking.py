
def my_sum(a,b,c):
    return a+b+c

list1 = [1,2,3]
list2 = [4,5,6]

combined = [list1, 'test' , *list2]
#combined = [*list1, 'test' , *list2]
print(combined)

print('-------------------------------')

def my_sum(*args):
    result =0
    for param in args:
        result += param
    return result

print(my_sum(10, 20, 30, 40, 50, 60))

print('-------------------------------')

def my_print(name, age, job):
    print(f'{name} is {age} years old and works as a {job}.')

dict1 = {'name': 'Mike', 'age': 35, 'job': 'programmer'}
dict2 = {'height': 185, 'weight':73 }

combined_dict = {**dict1, **dict2}

print(combined_dict)

def my_function(**kwargs):
    print('The following parameters were passed:')
    for k, v in kwargs.items():
        print(f'Parameter Name: {k}, Paramrter Value: {v}')

my_function(name='Mike', test='Hello' , other='World')