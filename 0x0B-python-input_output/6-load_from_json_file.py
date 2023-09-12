#!/usr/bin/python3
"""This module defines functoin a JSON file-reading """
import json


def load_from_json_file(filename):
    """Creates object a Python from a given (JSON) file"""
    with open(filename) as  f:
        return json.load(f)
