#!/usr/bin/python3

"""Module to find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function to find peak in list of integers"""

    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        # calculate the mid index
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # update high to mid, if true
            high = mid
        else:
            # update low to mid, if false
            low = mid + 1

    return list_of_integers[low]
