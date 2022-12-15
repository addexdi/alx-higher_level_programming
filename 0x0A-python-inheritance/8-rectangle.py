#!/usr/bin/python3
"""The module for class Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Initialize a new Rectangle class that inherits fron BaseGeometry"""

    def __init__(self, width: int, height: int) -> None:
        """Constructor for the Rectangle Class.
        Args:
        width: integer for rectangle width.
        height: integer for rectangle height.
        """
        self.__width = width
        self.__height = height
        super().integer_validator("height", height)
        super().integer_validator("width", width)
