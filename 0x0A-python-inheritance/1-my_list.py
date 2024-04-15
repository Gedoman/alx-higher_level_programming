#!/usr/bin/python3
""" module for MyList class."""


class MyList(list):
    """Mylist class"""
    def print_sorted(self):
        """Public instance method for printing
            s sorted list."""
        print(sorted(self))
