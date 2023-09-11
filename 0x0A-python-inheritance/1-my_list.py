#!/usr/bin/python3
'''Defines the inherited list class MyList..'''


class MyList(list):
    '''Implementes sorted printing of the built-in List class.'''

    def print_sorted(self):
        '''Print an ascending list..'''
        print(sorted(self))
