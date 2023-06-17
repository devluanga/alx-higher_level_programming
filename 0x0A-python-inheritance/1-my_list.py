#!/usr/bin/python3
''' Mylist inherits from list
'''


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        '''
        prints the sorted list
        '''
        print(sorted(self))
