#!/usr/bin/python3
"""Module documentation explaining the purpose of models.square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor/Initializer for the Square class"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes with the values passed as arguments"""

        if args and len(args) != 0:
            a = 0

            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)

                    else:
                        self.id = arg

                elif a == 1:
                    self.size = arg

                elif a == 2:
                    self.x = arg

                elif a == 3:
                    self.y = arg

                a += 1

        elif kwargs and len(kwargs) != 0:

            for k, v in kwargs.items():

                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)

                    else:
                        self.id = v

                elif k == "size":
                    self.size = v

                elif k == "x":
                    self.x = v

                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Override the default __str__ method"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
