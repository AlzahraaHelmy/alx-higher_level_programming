#!/usr/bin/python3
""" Defines a new class named Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for the Square class """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Returns a string representation of the Square """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.size)

    @property
    def size(self):
        """ Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns arguments to each attribute """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}
