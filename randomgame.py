from random import randint
import sys
#genrator a number
answer = randint(1,10)

#input from user


# cheack the input number 1~10
while True:
    try:
        guess = input('guess a number 1~10:  ')
        if int(guess) > 0 and int(guess) < 11:
            print("all good")
            break
        else:
            print("hey bozo, enter 1~10")
    except ValueError:
        print("please enter number")
        continue



