#!/usr/bin/python3
"""It contains the function "append_wrtie"."""



def append_write(filename="", text=""):
    """Returns the number of characters appended to 'filename' from 'text'
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
