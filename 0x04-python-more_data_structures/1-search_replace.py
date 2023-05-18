#!/usr/bin/python3
# function that replaces all occurrences of an element by another in a new list.

def search_replace(my_list, search, replace):
    return (list(map(lambda x: replace if x is search else x, my_list)))
