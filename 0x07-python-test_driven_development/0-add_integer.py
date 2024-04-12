#!/usr/bin/python3
""" Module for 0-add_integer"""


def add_integer(a, b=98):
    """this Function  add two an integer and return 
    their sum.
    usage:
    Raises:
        TypeError: if a, b are not int, float
    Raises:
        The sum of two integer.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
