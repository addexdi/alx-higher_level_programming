#!/usr/bin/python3
"""An empty rectangle module in python"""


class Rectangle:
    """Class that defines an empty rectangle module"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """Initializer for the class Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self) -> int:
        """Calculates the area and return the  Value"""
        return self.__height * self.__width

    def perimeter(self) -> int:
        """Calculates the perimeter and return the value"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        """Informal representation of class instance using #"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method for comparison"""
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __repr__(self):
        """Formal representation of the class Rectangle"""
        rect = "{self.__class__.__name__}({self.width},"
        rect += "{self.height})".format(self=self)

    def __del__(self):
        """Delete a class instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
