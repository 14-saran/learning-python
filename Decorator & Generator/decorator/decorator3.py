def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} return value {value}")
            f.write(f"{fname} return value {value}")
        return value
    
    return wrapper
@logged
def add(x,y):
    return x + y
print(add(10,20))



print('-----------------------------------------------')



#สร้าง decorator ที่เช็คสิทธิ์ผู้ใช้

def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user != 'admin':
            print(" No Permission")
            return
        return func(user, *args, **kwargs)
    return wrapper

@requires_admin
def delete_data(user):
    print(f"{user} ลบข้อมูลสำเร็จ")

delete_data('abcd')
delete_data('admin')

print('**-----------------------------------------------**')


    




