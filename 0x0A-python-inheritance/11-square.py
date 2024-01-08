#!/usr/bin/python3

"""7-base_geometry module"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value to be a positive int"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiates a Rectangle with given width and height"""

        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle"""

        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size):
        """Instantiates a Square with given size"""

        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

        def __str__(self):
            """Returns a string reps of the square"""

            return f"[Square] {self.__size}"
