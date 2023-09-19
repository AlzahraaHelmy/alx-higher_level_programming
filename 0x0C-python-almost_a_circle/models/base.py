#!/usr/bin/python3
""" Defines a Base class for JSON serialization """
from os import path
import json


class Base:
    """ Base class with methods for JSON serialization """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a Base instance with an optional 'id' """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        """ Converts a list of dictionaries to a JSON string """
        new = []
        if list_dict is None:
            return new
        else:
            return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves a list of objects to a JSON file """
        file_name = "{}.json".format(cls.__name__)
        new_list = []
        with open(file_name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_str):
        """ Converts a JSON string to a list of dictionaries """
        dictionary_list = []
        if json_str is None:
            return dictionary_list
        return json.loads(json_str)

    @classmethod
    def create(cls, **dict_args):
        """ Creates an instance with attributes set from a dictionary """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        if cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dict_args)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """ Loads a list of instances from a JSON file """
        instance_list = []
        return_empty = []
        file_name = "{}.json".format(cls.__name__)
        if path.isfile(file_name):
            with open(file_name, 'r') as file:
                instance_list = cls.from_json_string(file.read())
            for val in instance_list:
                return_empty.append(cls.create(**val))
            return return_empty
