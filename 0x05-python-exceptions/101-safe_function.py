#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        rn = fct(*args)
        return rn
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
