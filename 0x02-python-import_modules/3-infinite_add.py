#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    val = len(sys.argv) - 1
    count = 0

    for x in range(val):
	    count += int(sys.argv[x + 1])
    print("{}".format(count))
