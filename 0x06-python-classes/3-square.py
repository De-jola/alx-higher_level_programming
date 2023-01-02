#!/usr/bin/python3
"""Creating a Square class"""


class Square:
    """Represents a square, with size"""
    def __init__(self, size=0):
        """Initializing the data"""
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates and returns the value of area of square object instance
        """
        return self.__size * self.__size
