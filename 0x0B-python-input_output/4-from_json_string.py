#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a func JSON-to-object"""

import json


def from_json_string(my_str):
    """Return the Python obj representation of a JSON str"""

    return json.loads(my_str)
