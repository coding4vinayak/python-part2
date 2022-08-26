#error handling

while True:
    try:
        age = int(input("what is you age?"))
        10/age
    except ValueError:
        print('please enter number')
    except ZeroDivisionError:
        print('please enter number higher than 0')
    else:
        print("Thank you!")
        break
