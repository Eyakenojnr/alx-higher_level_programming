#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): size of a side of the square
        """
        self.__size = size

    @property
    def size(self):
        """Getter of __size
        Return: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of __size
        Args:
            value (int): size of a size of the square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculates area of a square
        Return: Current square area
        """
        return (self.__size) ** 2

    def my_print(self):
        """Prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                print('#' * self.__size)
