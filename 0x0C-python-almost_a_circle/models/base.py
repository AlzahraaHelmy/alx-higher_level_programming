#!/usr/bin/python3

"""Defines the base model class."""
import csv
import json
import turtle


class Base:
    """Base model.

    This represents the "base" for all other classes in the 0x0C project*.

    Special class attributes:
        __nb_object (int): The number of rules instantiated.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Configure a new rule.

        Args:
            id (int): New base identity.
        """
        if id is not None:
            Base.__nb_objects += 1
            self.id = id
        else:
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON sequence of the dictation list.

        Args:
            list_dictionaries (list): Dictionary list.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write a JSON serialization of the object list to a file.

        Args:
            list_objs (list): List of inherited primary instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return deserialized JSON string.

        Args:
            json_string (str): JSON string representation of the list of dictations.
        Returns:
            If json_string is None or empty - empty list.
            Otherwise - A Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instantiated class from the attribute dictionary.

        Args:
            **dictionary (dict): Key/value pairs are attributes to be initialized.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                nw = cls(1, 1)
            else:
                nw = cls(1)
            nw.update(**dictionary)
            return nw

    @classmethod
    def load_from_file(cls):
        """Returns a list of instantiated classes from a JSON stringed file.

        Reads from `<cls.__name__>.json`.

        Returns:
            If file does not exist - blank list.
            Otherwise - a list of the instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                l_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in l_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write a CSV sequence of the object list to a file.

        Args:
            list_objs(list): List of inherited underlying instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                wr = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    wr.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return the list of instantiated classes from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If file does not exist - blank list.
            Otherwise - a list of the instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the Turtle module.

          Media:
              list_rectangles(list): List of rectangular objects to be drawn.
              list_squares (list): A list of square objects to be drawn.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
