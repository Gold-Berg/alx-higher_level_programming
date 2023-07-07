#!/usr/bin/python3
"""
N-Queens Puzzle Solver
"""

import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at position (row, col) on the board
    """

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the same diagonal (left-top to right-bottom)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check if there is a queen in the same diagonal (left-bottom to right-top)
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False

    return True

def solve_nqueens(board, row):
    """
    Solve the N-Queens problem recursively using backtracking
    """

    # Base case: All queens are placed, print the solution
    if row == N:
        print_solution(board)
        return

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1

def print_solution(board):
    """
    Print the board configuration as a solution
    """

    solution = []
    for i in range(N):
        row = ['.'] * N
        row[board[i]] = 'Q'
        solution.append(''.join(row))
    print('\n'.join(solution))
    print()

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 (no queen)
    board = [-1] * N

    # Solve the N-Queens problem
    solve_nqueens(board, 0)
