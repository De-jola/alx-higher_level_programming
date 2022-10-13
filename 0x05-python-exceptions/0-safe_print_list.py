#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    while(y < x):
        try:
            print(my_list[y], end="")
        except IndexError:
            x = y
        y += 1
    print("")
    return x
