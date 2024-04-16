#!/usr/bin/python3
"""module for append_write method"""


def append_write(filename="", text=""):
    """append functaion"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
