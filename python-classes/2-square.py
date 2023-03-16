#!/usr/bin/python3
class Square:
    """Its crazy that we are not importing any modules"""
    
    def __init__(self, size=0):
        """Initialize a new instance of the Square class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

