#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_integar = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        is_integar = False
    return is_integar
