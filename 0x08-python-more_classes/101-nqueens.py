#!/usr/bin/bash
"""
N-Queens Problem Solver
"""

import sys

def is_safe(board, row, col, N):
    """
    Check if a queen can be placed at the specified position (row, col) on the board.
    """

    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, N):
    """
    Recursive function to solve the N-Queens problem using backtracking.
    """

    # Base case: If all queens are placed, print the solution
    if col == N:
        solution = [[row, col] for row in range(N) if board[row][col] == 1]
        print(solution)
        return

    # Recursive backtracking to try placing a queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, col + 1, N)
            board[row][col] = 0

def nqueens(N):
    """
    Solve the N-Queens problem for a given N.
    """

    # Check if N is an integer
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty N x N chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N-Queens problem
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command-line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
