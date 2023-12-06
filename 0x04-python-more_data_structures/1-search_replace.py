#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for elements in my_list:
        if elements == search:
            new_list.append(replace)
        else:
            new_list.append(elements)

    return new_list
