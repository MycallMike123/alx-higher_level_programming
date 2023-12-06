#!/usr/bin/python3

def uniq_add(my_list=[]):
    integer = set()

    for number in my_list:
        integer.add(number)

        result = sum(integer)

        return result
