#!/usr/bin/python3
"""Creating a class"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """initializing the data"""
        self.__size = size

    @property
    def size(self):
        """returns the value of size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """assigning a value to size"""
        if type(value) == int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must  be >= 0")

    def area(self):
        """claculates and returns the value of the area
        """
        return self.__size * self.__size
