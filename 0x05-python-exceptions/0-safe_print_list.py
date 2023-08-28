#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for True:
        try:
            if total < x:
                print(my_list[total], end='')
                total += 1
            else:
                print()
                return total
        except IndexError:
            print()
            return (total)
