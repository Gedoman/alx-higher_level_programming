#!/usr/bin/python3
"""module for Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass representing a rectangle"""
    def __init__(self, width, height):
        """constractor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
