import os

def collect_matrices():
    if os.path.exists("matrices.txt"):
        file = open("matrices.txt", mode="r").read().split("\n")
        m1 = ""
        m2 = ""
        c = 0
        for line in file:
            if line != "" and c == 0:
                m1 += line 
            else:
                c += 1
                m2 += line
        matrix1, matrix2 = eval(m1), eval(m2)
        row = len(matrix1)
        column = len(matrix2)
        row_2 = len(matrix2[0])
        return matrix1, matrix2, row, column, row_2
    else:
        raise TypeError("matrix.txt file is missing")

def check_matrices(matrix1, matrix2):
    if len([n for n in matrix1[0]]) == len(matrix2):
        return True
    else:
        return False
    
def output_matrices(matrix1, matrix2, A, B, C):
    print(f"first: {A}x{B}")
    for line in matrix1:
        print(*line)
    print(f"second: {B}x{C}") 
    for line in matrix2:
        print(*line)