#!/usr/bin/python3
"""This is a template for a base geometry class in python"""


class BaseGeometry:
    """A class for the BaseGeometry"""

    def area(self):
        """Empty initializer for class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(
                name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(
                name))
