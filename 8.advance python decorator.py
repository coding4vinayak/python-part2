#decorators
# decorator supercharge functions


#higher order function hoc
#eg
'''
def greet(func)
  func()                  # function accept another func iside its parametr


def greet2():              #function return another function
   def func()
    return  5
 return func

'''

#decorator

def my_decorator(func):
    def wrap_function():
        print("*********")
        func()
        print("*********")
    return wrap_function

@my_decorator
def hello():
    print("helloooo")

hello()

# what is happening underhood
#  just my_decorator(hello) is hapening


#  what if add argument in  func helllo
def my_decorator(func):
    def wrap_function(x):
        print("*********")
        func(x)
        print("*********")
    return wrap_function

@my_decorator
def hello(greeting):
    print(greeting)

hello('hiiiiii')


#decorator
from time import time
def performance(fn):
    def wrapeer(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'tool {t2 - t1}s')
        return result
    return wrapeer

@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()


