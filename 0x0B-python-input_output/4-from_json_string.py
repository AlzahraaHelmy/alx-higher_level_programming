#!/usr/bin/python3
"""
This module defines a function from string to JSON
"""


import json


def from_json_string(my_str):
    """Returns the JSON representation of a (string) object"""
    return json.loads(my_str)
