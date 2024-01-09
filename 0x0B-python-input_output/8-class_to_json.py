#!/usr/bin/python3
"""Defines a func Python class-to-JSON"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an obj"""

    return obj.__dict__
