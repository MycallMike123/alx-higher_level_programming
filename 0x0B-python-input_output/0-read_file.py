#!/usr/bin/python3
"""Defines a func text file-reading"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its content to stdout"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
