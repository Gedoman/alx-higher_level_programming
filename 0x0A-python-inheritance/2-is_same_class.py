#!/usr/bin/python3
""" module for is_same_class  mithod"""


def is_same_class(obj, a_class):
    """determines if an object is exactly an instance of class"""
    x = isinstance (obj, a_class)
    if x == True:
        return True
    else:
        return False
