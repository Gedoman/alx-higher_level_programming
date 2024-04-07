#!/usr/bin/python3
""" Square Modual"""

class Square:
    """Define a Square."""

    def __init__(self, size=0):
        """ Constructor.

        Arge:
            size : int
            length od a side of the square.

        raises:
            TypeError : if size is not an integer
            ValueError : if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


