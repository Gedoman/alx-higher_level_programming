#!/usr/bin/python3
"""function that deletes a key in a dictionary"""


def simple_delete(a_dictionary, key=""):
    if a_dictionary:
        try:
                del a_dictionary[key]
        except KeyError:
                pass
        return a_dictionary
