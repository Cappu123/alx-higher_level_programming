#!/usr/bin/python3
"""a class Square that defines a square"""

class Square():
    "a square class with its proper validation"""

    def __init__(self, size=0):
        self.__size = size

    """property to retrieve the private instance attribute size"""
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
