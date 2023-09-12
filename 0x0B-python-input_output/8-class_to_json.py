#!/usr/bin/python3
"""This module defines the Python class-to-JSON function"""


def class_to_json(obj):
    """Dictionary re-representation of a simple data structure"""
    return obj.__dict__
