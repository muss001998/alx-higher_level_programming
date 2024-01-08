#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """this Print a square with the # character.

    Args:
        size (int): reps The height/width of the square.
    Raises:
        TypeError: type error If size is not an integer.
        ValueError: type val error If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
