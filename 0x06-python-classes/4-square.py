#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of side of a square
    """
    def __init__(self, size=0):
        """Initializes the Square class
        Args:
            size (int): size of side of a square"""
        self.__size = size

    @property
    def size(self):
        """Getter of __size
        Return: size of the square side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of __size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculate's the square area
        Return: Area of the square
        """
        return (self.__size) ** 2
