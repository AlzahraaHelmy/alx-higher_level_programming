#!/usr/bin/python3
""" Defines a new class named Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor for the Rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter method for width """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter method for height """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter method for x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter method for x """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter method for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter method for y """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ Prints the Rectangle instance with the character # """
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ Assigns arguments to each attribute """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Returns a string representation of the Rectangle """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {'id': self.id, 'x': self.x, 'y': self.y,
                'width': self.width, 'height': self.height}
