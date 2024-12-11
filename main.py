from data import collect_matrix, output_matrices, check_matrices
from multiplication import multiplicate
from generation import generate_matrices

question = int(input("select a mode:\n1 - your matrices\n2 - generate random matrices\n! enter only a number !\n"))
if question == 1:
    print("-- ENTER THE FIRST MATRIX --")
    matrix1 = collect_matrix()

    print("-- ENTER THE SECOND MATRIX --")
    matrix2 = collect_matrix()
elif question == 2:
    matrix1, matrix2 = generate_matrices()

print("-- MATRICES --")
output_matrices(matrix1=matrix1, matrix2=matrix2, mode=question)

print("-- VALIDATE --")
if check_matrices(matrix1=matrix1, matrix2=matrix2, mode=question):
    print("! ok !")
    print("-- MATRIX MULTIPLICATION RESULT --")
    multiplicate(matrix1=matrix1, matrix2=matrix2, mode=question)
else:
    print("! entered data is incorrect !")