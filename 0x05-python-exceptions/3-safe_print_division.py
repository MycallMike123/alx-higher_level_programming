#!/usr/bin/python3

def safe_print_division(a, b):
    res = None

    try:
        res = a / b

    except ZeroDivisionError:
        print("None")

    except (TypeError, ValueError):
        print("None")

    finally:
        print("Inside result: {}".format(res))

        return res
