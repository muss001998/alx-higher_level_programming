#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """this Invert int operators == and !=."""

    def __eq__(self, value):
        """this Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """this Override != operator with == behavior."""
        return self.real == value
