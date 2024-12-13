from random import randint

def generate_matrix(width, height):
    matrix = list()
    for i in range(height):
        matrix.append([float(randint(1, 1000)) for i in range(width)])
    return matrix
