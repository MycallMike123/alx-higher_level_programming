#!/usr/bin/python3
"""Defines a func file-appending"""


def append_write(filename="", text=""):
    """Writes a string to a text file (UTF-8), returns no. of xters"""

    with open(filename, "a", encoding="utf-8") as file:
        c_count = file.write(text)

    return c_count
