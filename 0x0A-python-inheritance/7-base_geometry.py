#!/usr/bin/python3
"""module for BaseGeometry"""


class BaseGeometry:
    """A BaseGeometry class """
    def area(self):
        """method to compute this area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """method to that validates value"""
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<name> must be greater than 0")

