#!/usr/bin/python3
"""This function adds an item to the list at
a specific location"""
def replace_in_list(my_list, idx, element):
    """faunction that replace an element
      my_list: list to replace its element
      idx: int the index of element replace
      element: Any the new item
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_new_list=my_list
        my_new_list[idx]=element
        return my_new_list