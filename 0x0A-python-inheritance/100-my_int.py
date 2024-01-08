#!/usr/bin/python3

"""Module with myint class"""


class MyInt(int):
    """MyInt class, inherits from int with == and !="""

    def __eq__(self, other):
        """Inverts the == operator"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator"""

        return super().__eq__(other)
