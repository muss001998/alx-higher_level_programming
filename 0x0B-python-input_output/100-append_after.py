#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """this Insert text after each line containing a given string in a file.

    Args:
        filename (str):reps The name of the file.
        search_string (str):reps The string to search for within the file.
        new_string (str):reps The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
