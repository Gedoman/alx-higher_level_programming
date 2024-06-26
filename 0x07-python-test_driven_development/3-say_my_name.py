#!/usr/bin/python3
"""Modual for Say my name."""


def say_my_name(first_name, last_name=""):
    """Take the first name and last name(option) and return it.
    Args:
        first_name: string
        last_name: string
    Return:
        first_name + last_name
    Raises:
        TypeError: if last_name is not string
        TypeError: if first_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
