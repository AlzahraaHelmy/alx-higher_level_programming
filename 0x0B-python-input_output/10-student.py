#!/usr/bin/python3
""" create student class """


class Student:
    """ Defining a class of student"""
    def __init__(self, first_name, last_name, age):
        """ Initializing a class of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return a dictionary representation of class """
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
