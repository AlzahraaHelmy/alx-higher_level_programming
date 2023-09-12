#!/usr/bin/python3
"""
create the class "Student"
"""


class Student:
    """Representation of a class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student """
        return self.__dict__
