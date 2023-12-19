#!/usr/bin/python3

"""This module defines a class Square."""


class Square:
    """This class reps a square."""

    def __init__(self, size=0):
        """Init the Square instance with optional size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """Return the current square area."""

        return self.__size ** 2
