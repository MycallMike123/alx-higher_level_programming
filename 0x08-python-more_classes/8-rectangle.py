#!/usr/bin/python3

"""Module that defs a class rectangle"""


class Rectangle:
    """A class Rectangle def"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional w and h"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            lines = [
                    str(self.print_symbol) * self.__width
                    for _ in range(self.__height)
            ]
            return '\n'.join(lines)

    def __repr__(self):
        """Return a string representation for recreation using eval()"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a deletion message when an instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        else:
            return rect_2
