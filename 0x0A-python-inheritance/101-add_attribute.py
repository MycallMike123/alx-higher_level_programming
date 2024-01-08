#!/usr/bin/python3

"""Module that adds attribute"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
