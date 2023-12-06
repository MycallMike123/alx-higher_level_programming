#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    output = [[0 for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output[i][j] = matrix[i][j] ** 2

    return output
