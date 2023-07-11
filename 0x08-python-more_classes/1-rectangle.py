#!/usr/bin/python3
"""Defines the Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """initializes instance of the class."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
