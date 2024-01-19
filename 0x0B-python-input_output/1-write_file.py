#!/usr/bin/python3
"""Function Write Text In File"""


def write_file(filename="", text=""):
    """Write Function"""
    with open(filename, 'w') as file:
        return file.write(text)
