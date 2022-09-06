#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """Represents a recatnagle"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
            width(int): the width of the rectangle default to 0
            height(int): the height of the rectangle default to 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Defines the string representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectang = []
        for i in range(self.__height):
            [rectang.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rectang.append("\n")
        return "".join(rectang)
