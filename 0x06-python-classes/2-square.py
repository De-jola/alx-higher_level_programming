#!/usr/bin/python3
"""Creating a square class"""


class Square:
    """Represents a square with size"""
    def __init__(self, size=0):
        """Initializes the data"""
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
