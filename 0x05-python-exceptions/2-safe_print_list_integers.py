#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    prints = 0

    try:
        for elements in range(x):
            value = my_list[elements]

            if type(value) == int:
                print("{:d}".format(value), end="")

                prints += 1
    except (ValueError, TypeError):
        pass

    print()
    return prints
