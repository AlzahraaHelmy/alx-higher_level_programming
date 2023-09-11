#!/usr/bin/python3
"""
It has a search function
"""


def lookup(obj):
    """Returns a list of the available attributes and methods for the object"""
    return dir(obj)
