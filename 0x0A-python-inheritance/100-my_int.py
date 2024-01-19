#!/usr/bin/python3
"""Create Class That Inhertance From int"""


class MyInt(int):
    """Reverse Normal Behavior Of == and !="""

    def __eq__(self, val):
        """Function That Swap Equal To Not Equal"""
        return super().__ne__(val)
        # return self.real != val  => Another Way

    def __ne__(self, val):
        """Function That Swap Not Equal To Equal"""
        return super().__eq__(val)
        # return self.real == val  => Another Way
