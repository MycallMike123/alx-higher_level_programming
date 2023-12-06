#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    updated_dictionary = {key: value}

    a_dictionary.update(updated_dictionary)

    return a_dictionary
