#!/usr/bin/python3
"""Creating a class"""


class Square:
    """Represents a square with size"""
    def __init__(self, size=0):
        """initializing the data"""
        self.__size = size

    @property
    def size(self):
        """retrieving the size data"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting the value of size"""
        if type(value) == int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """"Calculates and returns the value of area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints out a square"""
        if self.__size == 0:
            print("")
        else:
            for x in range(0, self.__size):
                for y in range(0, self.__size):
                    print("#", end="")
                print("")
