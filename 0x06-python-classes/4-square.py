#!/usr/bin/python3

"""This module defines a class Square."""


class Square:
    """This class reps a square."""

    def __init__(self, size=0):
        """This initializes the square instance with option size."""

        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):
        """Return the current square area."""

        return self.__size ** 2
