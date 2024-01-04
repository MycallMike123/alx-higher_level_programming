#!/usr/bin/python3

"""Module that defs a class rectangle"""


class Rectangle:
    """A class Rectangle def"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional w and h"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with type and value checkes"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:

            self.__width = value

    @property
    def height(self):
        """Retrieves the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with type and value checks"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:

            self.__height = value

    def area(self):
        """Returns the area of a rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a rectangle"""

        if self.__width and self.__height:
            return 2 * (self.__width + self.__height)

        else:
            return 0

    def __str__(self):
        """Return a string representation of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""

        else:
            lines = ['#' * self.__width for _ in range(self.__height)]
            return '\n'.join(lines)
