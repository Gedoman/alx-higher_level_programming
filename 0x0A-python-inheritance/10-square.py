#!/usr/bin/python3
"""module for Rectangle class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """a subclass representing a rectangle"""
    def __init__(self, size):
        """constractor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method which return area of retangle"""
        return self.__size ** 2
