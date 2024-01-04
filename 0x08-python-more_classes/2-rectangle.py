#!/usr/bin/python3

"""Module that reps a class Rectangle"""


class Rectangle:
    """A class rectangle defination"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and h"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with type and val checks"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with type and value checks"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    def area(self):
        """Returns area of a rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a rectangle"""

        if self.__width and self.__height:
            return 2 * (self.__width + self.__height)

        else:

            return 0
