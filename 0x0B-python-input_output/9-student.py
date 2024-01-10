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

    def to_json(self):
        """this Get a dictionary representation of the Student."""
        return self.__dict__
