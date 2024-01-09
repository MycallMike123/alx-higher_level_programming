#!/usr/bin/python3
"""Defines a func text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific str"""

    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, mode="w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
