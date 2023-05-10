#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
val = abs(num) % 10
if num < 0:
    val = -val
print("Last digit of {} is {} and is ".format(num, val), end="")
if val > 5:
    print("greater than 5")
elif val == 0:
    print("0")
else:
    print("less than 6 and not 0")