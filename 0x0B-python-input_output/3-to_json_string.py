#!/usr/bin/python3
"""This module defines a function from string to JSON"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a (string) object"""
    return json.dumps(my_obj)
