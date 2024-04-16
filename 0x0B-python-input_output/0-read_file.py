#!/usr/bin/python3
"""module of def read_file method"""


def read_file(filename=""):
    """red the file
    Args: 
        filename: file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
