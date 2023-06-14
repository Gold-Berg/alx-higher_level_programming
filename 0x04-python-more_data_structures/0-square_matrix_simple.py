#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    aws = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            aws[i][j] = matrix[i][j] ** 2

    return result
