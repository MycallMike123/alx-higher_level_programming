#!/usr/bin/python3
"""Defines a func JSON file-reading"""

import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file"""

    with open(filename) as file:
        return json.load(file)
