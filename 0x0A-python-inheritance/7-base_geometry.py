#!/usr/bin/python3

"""A module with the class Base geometry"""


class BaseGeometry:
    """A class representing the base geometry"""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the values"""

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
