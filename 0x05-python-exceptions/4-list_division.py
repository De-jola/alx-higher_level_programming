#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for x in range(len(my_list_2)):
            try:
                result = my_list_1[x] / my_list_2[x]
                new_list.append(result)
            except ZeroDivisionError:
                print("division by 0")
                result = 0.0
                new_list.append(result)
            except TypeError:
                print("wrong type")
                result = 0.0
                new_list.append(result)
            except IndexError:
                print("out of range")
                result = 0.0
                new_list.append(result)
    finally:
        return(new_list)
