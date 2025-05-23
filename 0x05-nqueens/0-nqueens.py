#!/usr/bin/python3
"""Solves the N queens problem.
"""

import sys


def is_safe(board, row, col, N):
    """Check if a queen can be placed at board[row][col]"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(row, board, solutions, N):
    """Recursively place queens and collect valid solutions"""
    if row == N:
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(row + 1, board, solutions, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * N
    solve_nqueens(0, board, solutions, N)

    for solution in solutions:
        print(solution)
