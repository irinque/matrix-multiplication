from sys import stdin

def collect_matrix():
    matrix = list()
    previous_line = ""
    for line in stdin:
        if previous_line == "":
            previous_line = line
        if len(previous_line.split()) == len(line.split()):
            matrix.append(line.rstrip("\n"))
            previous_line = line
        elif line == "\n":
            break
        else:
            print("warning: the string is not saved. the number of elements is not equal.")
    return matrix

def check_matrices(matrix1, matrix2):
    if len([n for n in matrix1[0].split() if n.isnumeric()]) == len(matrix2):
        return True
    else:
        return False

def output_matrices(matrix1, matrix2):
    print("first:", *matrix1, sep="\n", end="\n")
    print("second:", *matrix2, sep="\n", end="\n") 