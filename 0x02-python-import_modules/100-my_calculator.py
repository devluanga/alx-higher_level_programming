#!/usr/bin/python3

from calculator_1 import *
import sys

if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    calops = {"+": add, "-": sub, "*": mul, "/": div }
    if sys.argv[2] not in list(calops.keys()):
	    print("Unknown operator. Available operators: +, -, * and /")
	    sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, calops[sys.argv[2]](a, b)))
