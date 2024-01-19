#!/usr/bin/python3
"""Function That Appends String In The End Of Text File"""


def append_write(filename="", text=""):
    """Append Text In The End Of Line"""
    with open(filename, "a") as file:
        return file.write(text)
