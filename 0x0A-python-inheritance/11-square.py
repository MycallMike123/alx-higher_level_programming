#!/usr/bin/python3

"""7-base_geometry module"""


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size):
        """Instantiates a Square with given size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
