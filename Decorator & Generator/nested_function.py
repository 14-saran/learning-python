

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()


print('-----------------------------------------')


def outer_function(text):
    def inner_function():
        print(text)
    inner_function()
outer_function("Hello world")



print('-----------------------------------------')


def pop(list1):
    def get_last_element(list2):
        return list1[len(list2)-1]
    list1.remove(get_last_element(list1))
    print(list1)
    return(list1)

list_of_numbers = [1,2,3,4,5,6]
pop(list_of_numbers)
pop(list_of_numbers)
