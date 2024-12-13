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
        matrix1, matrix2 =  [[float(num) for num in lst] for lst in eval(m1)], [[float(num) for num in lst] for lst in eval(m2)]
        dimension_a = len(matrix1)
        dimension_b = len(matrix2)
        dimension_c = len(matrix2[0])
        return matrix1, matrix2, dimension_a, dimension_b, dimension_c
    else:
        raise FileNotFoundError("matrices.txt file is missing")

def validate_dimensions(matrix1, matrix2):
    if len([n for n in matrix1[0]]) == len(matrix2):
        return True
    else:
        return False
    
def output_matrices(matrix1, matrix2, dimension_a, dimension_b, dimension_c):
    print(f"first: {dimension_a}x{dimension_b}")
    for line in matrix1:
        print(*line)
    print(f"second: {dimension_b}x{dimension_c}") 
    for line in matrix2:
        print(*line)