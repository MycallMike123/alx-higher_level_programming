#!/usr/bin/python3
"""Defines a func text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific str"""

    text_file = ""
    with open(filename) as rd:
        for line in rd:
            text_file += line

            if search_string in line:
                text_file += new_string

    with open(filename, "w") as w:
        w.write(text_file)
