#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """this Represent a student."""

    def __init__(self, first_name, last_name, age):
        """this Initialize a new Student.

        Args:
            first_name (str):reps The first name of the student.
            last_name (str):reps The last name of the student.
            age (int):reps The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this Gets a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional)reps The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """this Replaces all attributes of the Student.

        Args:
            json (dict):reps The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
