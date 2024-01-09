#!/usr/bin/python3
"""Defines a func file-writing"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8)"""

    with open(filename, "w", encoding="utf-8") as file:
        count_chars = file.write(text)

    return count_chars
