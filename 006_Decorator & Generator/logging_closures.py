import logging
logging.basicConfig(filename="example.log",level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info("Running '{}' wiht argument {}".format(func.__name__,args))
        print(func(*args))
    return log_func

def add (x,y):
    return x + y 

def sub (x,y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(8,3)
sub_logger(10,3)