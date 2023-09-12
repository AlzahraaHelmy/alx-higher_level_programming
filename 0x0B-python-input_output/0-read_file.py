#!/usr/bin/python3
"""This module defines the function of reading text files"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
