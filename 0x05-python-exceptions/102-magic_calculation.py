#!/usr/bin/python3
def magic_calculation(a, b):
    per = 0
    for index in range(1, 3):
        try:
            if index > a:
                raise Exception('Too far')
            else:
                per += (a ** b) / index
        except BaseException:
            per = b + a
            break
    return per
