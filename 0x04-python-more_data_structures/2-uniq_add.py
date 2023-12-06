#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    uniq_numbers = set()

    for num in my_list:
        if num not in uniq_numbers:
            result += num
            uniq_numbers.add(num)
    return result
