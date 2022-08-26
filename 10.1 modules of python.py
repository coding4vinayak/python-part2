#if __name__ = '__main__': #only run main module not other imported

#built in modules

import random
print(dir(random))
print(random.random())

from random import  shuffle
my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

import sys
