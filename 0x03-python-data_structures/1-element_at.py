#!/usr/bin/python3
def element_at(my_list, idx):
    num_of_elements = len(my_list)
    if (idx < 0) or (idx > num_of_elements - 1):
        return None
    return my_list[idx]
