import time
from random import randint

def generate_matrix(width, height):
    start = time.time()
    matrix = list()
    for i in range(height):
        matrix.append([float(randint(1, 1000)) for i in range(width)])
    finish = time.time()
    runtime = finish - start
    return matrix, runtime
