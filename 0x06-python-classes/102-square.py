#!/usr/bin/python3

"""Module of aClass representing a square."""


class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int or float): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation."""

        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""

        return self.__size ** 2

    def __eq__(self, other):
        """Define equality based on the square area."""

        return self.area() == other.area()

    def __ne__(self, other):
        """Define inequality based on the square area."""

        return self.area() != other.area()

    def __gt__(self, other):
        """Define greater than based on the square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define greater than or equal to based on the square area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Define less than based on the square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define less than or equal to based on the square area."""

        return self.area() <= other.area()
