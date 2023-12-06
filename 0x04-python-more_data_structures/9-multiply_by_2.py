#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multiply_dict = dict(a_dictionary)

    for key in multiply_dict:
        multiply_dict[key] = multiply_dict[key] * 2

    return multiply_dict
