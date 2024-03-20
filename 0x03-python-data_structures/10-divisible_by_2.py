#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    listrez = []
    for x in my_list:
        if (x % 2) == 0:
            listrez.append(True)
        else:
            listrez.append(False)
    return listrez
