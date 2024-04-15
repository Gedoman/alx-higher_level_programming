#!/usr/bin/python3
"""modual for lookup method."""


def lookup(obj):
    """looks up attributes and methods.
    Args:
        obj (object): the object to the list
    Ruturn:
        list: the list of attributes.
    """
    return dir(obj)
