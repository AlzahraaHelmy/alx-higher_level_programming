#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): first name to print.
        last_name (str):  last name to print.
    Raises:
        TypeError: If neither of first_name nor last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("Your name is {} {}".format(first_name, last_name))
