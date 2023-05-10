#!/usr/bin/python3
"""the function checks for a lowecase character
   rototype: def islower(c):
   Returns True if c is lowercase
   Returns False otherwise
   You are not allowed to import any module
   You are not allowed to use str.upper() and str.isupper()
"""
def islower(x):
    if ord(x) >= 97 and ord(x) <= 122:
        return True
    else:
        return False
