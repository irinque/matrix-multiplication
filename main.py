from data import collect_matrix, output_matrices, check_matrices
from multiplication import multiplicate

print("-- ENTER THE FIRST MATRIX --")
matrix1 = collect_matrix()

print("-- ENTER THE SECOND MATRIX --")
matrix2 = collect_matrix()

print("-- MATRICES --")
output_matrices(matrix1=matrix1, matrix2=matrix2)

print("-- VALIDATE --")
if check_matrices(matrix1=matrix1, matrix2=matrix2):
    print("! ok !")
    print("-- MATRIX MULTIPLICATION RESULT --")
    multiplicate(matrix1=matrix1, matrix2=matrix2)
else:
    print("! entered data is incorrect !")