#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    num = len(my_list)
    for x in range(num):
        new_list.append(my_list[x])
    if (idx < 0) or (idx > len(new_list) - 1):
        return new_list
    new_list[idx] = element
    return new_list
