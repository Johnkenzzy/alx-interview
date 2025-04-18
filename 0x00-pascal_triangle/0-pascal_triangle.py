#!/usr/bin/python3
"""
Defines pascal_triangle function
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])  # Sum numbers
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
