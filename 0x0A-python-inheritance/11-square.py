#!/usr/bin/python3
"""Module template for Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square for making square objects that inherits\
         attribute functions from Rectangle"""

    def __init__(self, size):
        """cONSTRUCTOR METHOD FOR SUARE
        Args:
        size(int): size of the square.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
