#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = my_list[:]

    for number, integer in enumerate(my_list):
        if integer % 2 == 0:
            result[number] = True
        else:
            result[number] = False
    return result
