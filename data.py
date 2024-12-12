from sys import stdin

def collect_matrices():
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
    return matrix1, matrix2


def check_matrices(matrix1, matrix2):
    if len([n for n in matrix1[0]]) == len(matrix2):
        return True
    else:
        return False
    
def output_matrices(matrix1, matrix2):
    print("first:")
    for line in matrix1:
        print(*line)
    print("second:") 
    for line in matrix2:
        print(*line)