#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        key = ""
        best_val = 0
        for i in my_list:
                if a_dictionary[i] > best_val:
                    best_val = a_dictionary
                    key = i
        return key
