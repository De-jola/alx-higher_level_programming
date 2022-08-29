#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    num = len(my_list)
    for x in range(num + 1):
        if (x == 0):
            continue
        print("{:d}".format(my_list[-x]))
