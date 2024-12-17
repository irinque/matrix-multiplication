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
        print(m1)
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
    
def output_matrices(matrix1, matrix2):
    file = open("matrices.txt", "w")
    for line in matrix1:
        file.write(f"{line},\n")
    file.write("\n")
    for line in matrix2:
        file.write(f"{line},\n")
    file.close()

def output_result(matrix):
    file = open("result.txt", "w")
    for line in matrix:
        file.write(f"{line},\n")
    file.close()