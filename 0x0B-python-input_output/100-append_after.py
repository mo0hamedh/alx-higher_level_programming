#!/usr/bin/python3
"""Define Function That Append After Last Line"""


def append_after(filename="", search_string="", new_string=""):
    """Append Function"""
    text = ''
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as write_file:
        write_file.write(text)
