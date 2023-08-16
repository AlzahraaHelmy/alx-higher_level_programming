#!/usr/bin/python3


def roman_to_int(rn_string):
    if not rn_string or type(rn_string) != str:
        return 0
    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(rn_string):
        arabic = digits[roman]
        total += arabic if total < arabic * 5 else -arabic
    return total
