#!/usr/bin/python3
""" module for class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """x of this rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """y of this rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """method for validating the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Calculate the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """prints string representation of rectangle"""
        s = "\n" * self.y + \
            (" " * self.x + "#" * self.width + "\n") * self.height
        print(s, end=" ")

    def __str__(self):
        """return string info about this rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   sels.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """internal method that update istance attributes"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """updates instance attributes via no-keyword & keyword args"""
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
