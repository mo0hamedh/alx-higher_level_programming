#!/usr/bin/python3
"""Create Class"""


class BaseGeometry:
    """Empty Class"""

    def __init__(self):
        pass

    def area(self):
        """Public Instance Method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check Validation Function"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
