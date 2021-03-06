import numpy as np
import random


def generate_gilbert_matrix(k):
    matrix = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            matrix[i][j] = 1 / (i + j + 1)

    return np.array(matrix)

def generate_diagonal_matrix(k):
    values = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    noise = 10 ** (-k)
    matrix = np.zeros((k, k))
    for i in range(k):
        for j in range(i, k):
            matrix[i][j] = matrix[j][i] = random.choice(values)

    for i in range(k):
        matrix[i][i] = -(sum(matrix[i]) - matrix[i][i]) + noise

    return np.array(matrix)

def generate_random_symmetric(k):
    matrix = np.zeros((k, k))
    for i in range(k):
        for j in range(i, k):
            matrix[i][j] = matrix[j][i] = random.random() * random.randint(-5, 5)

    return np.array(matrix)