#!/usr/bin/python3
"""A function that calculates the average
of the elements and returns it"""


def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return(sum(a * b for a, b in my_list) / sum(b for a, b in my_list)i
