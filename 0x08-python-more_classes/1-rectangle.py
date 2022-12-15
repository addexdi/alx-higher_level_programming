#!/usr/bin/python3
"""An empty rectangle module in python"""


class Rectangle:
    """Class that defines an empty rectangle module"""

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """Initializer for the class Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Setter function for width attribute which is a private attribute"""
        return self.__width

    @width.setter
    def width(self, value: int) -> int:
        """Getter function for the width private attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Setter function for height attribute which is a private attribute"""
        return self.__height

    @height.setter
    def height(self, value: int) -> int:
        """Getter function for the height private attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
