#!/usr/bin/python3
"""Defines The Function That Print Square"""


def print_square(size):
    """Print Square Function"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        [print('#', end='') for _ in range(size)]
        print("")
