#!/usr/bin/env python3
"""Rotate 2D Metrix Module
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise
    """
    m_len = len(matrix)

    for i in range(m_len):
        for j in range(i + 1, m_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
