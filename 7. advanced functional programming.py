# pure function

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([2,4,6]))


#map filter, zzip and reduce

#map      create new list
def multiply_by3(item):
    return item*3

print(list(map(multiply_by3,[2,3,4])))

#filter          this also make new list dont change original as map

my_list = [2,3,4]
def multiply_by3(item):
    return item*3

def only_odd(item):
    return item % 2 != 0     #removing even number

print(list(filter(only_odd, my_list)))
print(my_list)

#zip

my_list = [2,3,4]
your_list = [10,20,30]
def multiply_by4(item):
    return item*4

def only_odd(item):
    return item % 2 != 0

print(list(zip(my_list, your_list)))

#reduce
from  functools import reduce
my_list2 = [2,3,4]

def multiply_by5(item):
    return item*4

def only_even(item):
    return item % 2 == 0

def accumalator(acc, item):
    print(acc, item)
    return  acc + 1

print(reduce(accumalator, my_list2, 0))


#lambda expression

my_list3 = [2,3,4]

print(list(map(lambda item: item*2, my_list3 ))) #this expression doesnt save function i.e one time
print(list(filter(lambda item: item % 2 != 0, my_list3)))

#lambda exersise
#square
my_list4 = [5,4,3]

print(list(map(lambda item: item**2, my_list4)))

#sorting

a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key = lambda x: x[1])
print(a)

#list comprahansion

a_list = [char for char in 'hello']
print(a_list)

a_list2 = [num for num in range(0,100)]
print(a_list2)

a_list3 = [num*2 for num in range(0,100)]
print(a_list3)

a_list4 = [num**2 for num in range(0 , 100) if num % 2 ==0]
print(a_list4)

#set and dictionary comprahansion
a_set = {char for char in 'hello'}
print(a_set)

#dictionary
simple_dic ={
    'a': 1,
    'b': 2
}
my_dic = {key:value**2 for key, value in simple_dic.items() if value % 2 ==0}
print(my_dic)
