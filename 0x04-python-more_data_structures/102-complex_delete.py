#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    keys = []
    for k, v in a_dictionary.items():
        if v == value:
                keys.append(k)
    for x in keys:
        del a_dictionary[x]
    return a_dictionary
