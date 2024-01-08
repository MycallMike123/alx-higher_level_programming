#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """Returns a list of available attributesand methods of an object"""

    return (dir(obj))
