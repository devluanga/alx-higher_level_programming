#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    val = len(sys.argv) - 1
    """getting the number of arguments"""
    if val == 0:
        print("0 arguments")
    elif val == 1:
        print("1 argument.")
    else:
        print("{} arguments ".format(val))
    
    """getting list of arguments"""
    for x in range(val):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))