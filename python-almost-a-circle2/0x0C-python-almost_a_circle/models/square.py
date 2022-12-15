#!/usr/bin/python3
"""Square boiler plate that inherits from Rectangle()"""
from rectangle import Rectangle


class Square(Rectangle):
    """Square class; inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer for square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method"""
        return self.width

    @size.setter
    def size(self, size):
        """setter method"""
        self.width = size
        self.height = size

    def __str__(self):
        """Informal representation of a class"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates attribute for square class"""
        attrs = ("id", "size", "x", "y")
        if args:
            if len(args) > len(attrs):
                msg = "update() takes at max {} positional arguments but {} was given"
                raise TypeError(msg.format(len(attrs), len(args)))
            for ch in range(min(len(attrs), len(args))):
                setattr(self, attrs[ch], args[ch])

        else:
            for k in kwargs:
                if k not in attrs:
                    msg = "update() takes at max {} positional arguments but {} was given"
                    raise TypeError(msg.format(len(attrs), len(args)))

                setattr(self, k, kwargs.get(k))

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
