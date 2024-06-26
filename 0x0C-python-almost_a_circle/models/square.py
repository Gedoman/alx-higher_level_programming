#!/usr/bin/python3
"""module from Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string info about this square"""
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size of this square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """internal method that updates instance attributes via */**args"""
        if id is not = None:
            self.id = id
        if size is not = None:
            self.size = size
        if x is not = None:
            self.x = x
        if y is not = None:
            self.y = y

    def update(self, *args, **Kwargs):
        """updates instance attributes via no-keywped & keyword args"""
        if args:
            self.__update(*args)
        elif Kwargs:
            self.__update(**Kwargs)

    def to_dictionary(self):
        """"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
