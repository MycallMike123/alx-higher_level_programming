#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    prints = 0

    try:
        for elements in range(x):
            print(my_list[elements], end='')
            prints += 1

    except IndexError:
        pass

    print()  # A new line
    return prints
