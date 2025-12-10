#!/usr/bin/python3
"""A Square class"""


class Square:
    """inside"""

    def __init__(self, size=0):
        size(size)

    def size(self, value=0):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size*self.__size
