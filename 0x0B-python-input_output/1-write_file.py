#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """this Writes a string to a UTF8 text file.

    Args:
        filename (str):reps The name of the file to write.
        text (str):reps The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
