#!/usr/bin/python3
'''Defines a class called MyList
'''


class MyList(list):
    '''MyList inherits from list
    '''
    def print_sorted(self):
        '''Prints the sorted in asceding order
        '''
        print(sorted(self, reverse=False))
