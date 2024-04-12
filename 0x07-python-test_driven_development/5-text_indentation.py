#!/usr/bin/python3
"""Moduale of Text indentation method"""


def text_indentation(text):
    """Method for adding two new line after '. ? :' chars.
    Args:
        text: string
            the string text.
    Raise:
        TypeError: if text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for x in ".?:":
        text = (x + "\n\n").join(
                [line.strip(" ") for line in text.split(x)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
