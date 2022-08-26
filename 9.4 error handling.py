# error handling 3
while True:
    try:
        age = int(input("what is you age?"))
        10/age
        raise ValueError("hey cut it out")
        continue
    except ZeroDivisionError:
        print('please enter number higher than 0')
        break
    else:
        print("Thank you!")
        break
    finally:
        print('ok i am finally done')
