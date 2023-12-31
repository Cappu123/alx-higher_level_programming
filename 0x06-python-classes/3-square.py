#!/usr/bin/python3
"""class Square that defines a square"""

class Square():
    """square class with its proper validations"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """an instance that returns the current square area"""
        return self.__size ** 2
