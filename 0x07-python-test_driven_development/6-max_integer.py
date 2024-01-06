#!/usr/bin/python3


def max_integer(list=[]):
    """Show max """

    if len(list) == 0:
        return None
    res = list[0]

    a = 1

    while a < len(list):
        if list[a] > res:
            res = list[a]
        a += 1

    return res
