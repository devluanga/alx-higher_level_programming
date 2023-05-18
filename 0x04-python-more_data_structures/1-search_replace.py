#!/usr/bin/python3
#Write a function that replaces all occurrences of an element by another in a new list.

def search_replace(my_list, search, replace):
    newl = my_list[:]
    for val in range(len(newl)):
        if newl[val] == search:
            newl[val] = replace
    return (newl)
