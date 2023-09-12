#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a student."""


def __init__(self, first_name, last_name, age):
    """Initialize a new Student.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.
        age (int): The age.

    Raises:
        TypeError: If `age` is not an integer.

    """
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self):
    """Return the dictionary representation of a Student."""
    return self.__dict__
