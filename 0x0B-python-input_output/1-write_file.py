#!/usr/bin/python3
""" module for write_file method"""


def write_file(filename="", text=""):
    """writ on the file
    Args:
        filename: file
        text:text will me added in the file
    """
    with open(filename,encoding="utf-8") as file:
       return file.write(text)
