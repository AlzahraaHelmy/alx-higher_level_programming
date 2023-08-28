#!/usr/bin/python3
def magic_calculation(a, b):
    per = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                per += (a ** b) / i
        except:
            per = b + a
            break
    return per
