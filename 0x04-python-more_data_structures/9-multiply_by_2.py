#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dec = {}
    if a_dictionary:
        for k, v in a_dictionary.items():
                new_dec.update({k: v * 2})
    return new_dec
