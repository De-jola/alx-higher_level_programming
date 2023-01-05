#!/usr/bin/python3
"""This documentation is always available
    Creating a function that adds two integers
    This module containing the function \
    would be tested using Test Driven Development

    """


def add_integer(a, b=98):
    """Adding two integers
        returning the sum when inputs are numbers/floats
        Else raising an error"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
