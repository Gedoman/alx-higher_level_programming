#!/usr/bin/python3
"""
define a class Rectangle
"""


class Rectangle:
    """Representtation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width
    @width.set
    def width(self, value):
        """setter for the prived instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.set
    def height(self, value):
        """setter for the prived instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__width = value