#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    final_matrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        new_row = []
        for num in i:
            if type(num) is not int and type(num) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(num / div, 2))
        final_matrix.append(new_row)
    return final_matrix
