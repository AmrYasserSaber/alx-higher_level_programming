#!/usr/bin/python3
"""python file"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
