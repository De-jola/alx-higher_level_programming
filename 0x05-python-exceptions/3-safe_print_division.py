#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = 0
        result = a / b
        return a / b
    except ZeroDivisionError:
        result = None
        return None
    finally:
        print("Inside result: {}".format(result))
