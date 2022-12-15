#!/usr/bin/python3

class Rectangle:
    def __init__(self, x, y):
        if x < 0:
            raise ValueError("x cannot be negative")
        else:
            self.__x = x
        if y < 0:
            raise ValueError("y cannot be negative")
        else:
            self.__y = y

    def printf(self):
        print(self.__class__)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


r1 = Rectangle(10, 10)
r1.printf()
