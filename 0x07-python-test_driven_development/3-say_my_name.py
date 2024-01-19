#!/usr/bin/python3
"""Defines The Function That Prints The Name"""


def say_my_name(first_name, last_name=""):
    """print a name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
