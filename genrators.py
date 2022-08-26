#genrator
#range

#iterable are under the hood using __iter__
#iterate
#genrators (genrator are subset of uterable)

  #  def make_list(num):
  #  result = []
  #  for i in range( num):
  #  result.append(i*2)
  #  return  result

   # my_list = make_list(1000)
   # print(list(range(1000000)))


#genrator

def genrator_function(num):
    for i in range(num):
        yield i

for item in genrator_function(1000):
    print(item)


#fibbonachi
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield  a
        temp = a
        a = b
        b = temp + b

for x in fib(1000):
    print(x)