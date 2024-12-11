from random import randint

def generate_matrices():
    width = randint(1, 7)
    height = randint(1, 7)

    matrix1 = list()
    for i in range(height):
        matrix1.append([randint(1, 1000) for i in range(width)])
    matrix2 = list()
    for i in range(width):
        matrix2.append([randint(1, 1000) for i in range(height)])
    return matrix1, matrix2
