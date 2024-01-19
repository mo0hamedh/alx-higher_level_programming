#!/usr/bin/python3
"""This Is MyList Class"""


class MyList(list):
    """ subclass of list"""

    def print_sorted(self):
        """Sorted Method"""
        print(sorted(self))
