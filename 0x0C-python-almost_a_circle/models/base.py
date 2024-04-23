#!/usr/bin/pythom3
""" module for class"""
import json


class Base:
    """a representation of the base of our hierarchy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """jsonifies a dictionary so its quite rightly and longer"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves jsonified object to file"""
        if list_objs is not None:
            list_objs = [x.to_json_string() for x in list_objs]
        with open("{}.json".format(cls.__name__), "w",encoding="utf-8") as file:
                file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or  not json_string:
            return "[]"
        else:
             return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """loads instance form dictinary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1, 1)
        else:
            new = None
        new.update(**dictionary)
        return new


    @classmethod
    def load_from_file(cls):
        """loads string from file and unjsonifies"""
        from os import path

        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**x) for x in cls.from_json_string(f.read())]

