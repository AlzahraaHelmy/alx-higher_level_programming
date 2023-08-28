#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        per = a / b
    except ZeroDivisionError:
        per = None
    finally:
        print("Inside result: {}".format(per))
    return per
