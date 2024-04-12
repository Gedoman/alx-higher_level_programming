#!/usr/bin/python3
"""Module for Matrix_devided method."""


def matrix_divided(matrix, div):
    """Divided all elements of matrix by div.
    Args:
        matrix: list
            list of list containing int or float items
        div: number to divide matrix
    returns:
        list: int or float
            list of lists cratid from divided matrix.
    raises:
        TypeError:  if div is not  a number (integer or float)
        TypeError:  if Each row of the matrix is not the same size
        TypeError:  if matrix is not a list of lists of integers or floats
        ZeroDivisionError:  if div  equal to zero
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")
    for Row in matrix:
        if not isinstance(Row, list) or len(Row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            "of integers/floats")
        if len(Row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in Row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")
    return [[round(item / div, 2) for item in Row] for Row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
