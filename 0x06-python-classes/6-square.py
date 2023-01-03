#!/usr/bin/python3
"""Creating a class"""


class Square:
    """Represents a square with size and position"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing the data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieveing the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Assigning a value to self.__size"""
        if type(value) == int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """retrieveing the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the value for the position"""
        if type(value) == tuple and value > 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculates and returns the value of the area"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square object"""
        if self.__size == 0:
            print("")
        for x in range(0, self.__size):
            if self.__position[1] == 0:
                print("_"*self.__position[0], end="")
            for y in range(0, self.__size):
                print("#", end="")
            print("")
