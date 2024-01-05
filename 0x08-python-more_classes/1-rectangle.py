#!/usr/bin/python3
"""this defines a Rectangle class."""


class Rectangle:
    """this represent a rectangle."""

    def __init__(self, width=0, height=0):
        """this Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """this will Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width here must be an integer")
        if value < 0:
            raise ValueError("width here must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(" this height must be an integer")
        if value < 0:
            raise ValueError("height here must be >= 0")
        self.__height = value