#!/usr/bin/python3
"""
Contain the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance of or inherited from a_class, otherwise false"""
    return (isinstance(obj, a_class))
