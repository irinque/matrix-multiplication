def check_matrices(matrix1, matrix2):
    if len(matrix1) == len(matrix2[1].split()) or len(matrix2) == len(matrix1[1].split()):
        return True
    else:
        return False