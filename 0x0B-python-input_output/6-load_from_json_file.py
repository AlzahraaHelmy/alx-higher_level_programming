#!/usr/bin/python3
"""This module defines functoin a JSON file-reading."""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - loading an object from JSON file.
    Args:
        filename: the name of the file
    """
    with open(filename, "r") as  f:
        return json.load(f)
