#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numval = 0
if number < 0:
    number *= -1
    numval = 1
lastd = number % 10
if numval == 1:
    number *= -1
    fval *= -1
print("Last digit of {:d} is ".format(number), end="")
if fval > 5:
    print("{:d} and is greater than 5".format(fval))
elif fval == 0:
    print("{:d} and is 0".format(fval))
else:
    print("{:d} and is less than 6 and not 0".format(fval))
