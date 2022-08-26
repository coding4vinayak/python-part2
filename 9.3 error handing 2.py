
def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)

print(sum(1,0))
print(sum(1,'w'))



#exersise

while True:
    try:
        age = int(input("what is you age?"))
        10/age
    except ValueError:
        print('please enter number')
        continue
    except ZeroDivisionError:
        print('please enter number higher than 0')
        break
    else:
        print("Thank you!")
        break
    finally:
        print('ok i am finally done')
    print("can you here me")


# error handling 3
while True:
    try:
        age = int(input("what is you age?"))
        10/age
        raise ValueError
        continue
    except ZeroDivisionError:
        print('please enter number higher than 0')
        break
    else:
        print("Thank you!")
        break
    finally:
        print('ok i am finally done')
    print("can you here me")