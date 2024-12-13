import argparse
import random
from data import collect_matrices, output_matrices, check_matrices
from multiplication import multiplicate
from generation import generate_matrix


parser = argparse.ArgumentParser(description="select a mode:")
parser.add_argument("mode", type=int, help="1 - your matrices from file\n2 - generate random matrices")
args = parser.parse_args()

print("--- MATRICES ---")
if args.mode == 1:
    matrix1, matrix2, row, column, row_2 = collect_matrices()
    output_matrices(matrix1=matrix1, matrix2=matrix2, A=row, B=column, C=row_2)
elif args.mode == 2:
    row = random.randint(1, 12)
    column = random.randint(1, 12)
    row_2 = random.randint(1, 12)
    matrix1 = generate_matrix(width=column, height=row)
    matrix2 = generate_matrix(width=row_2, height=column)
    output_matrices(matrix1=matrix1, matrix2=matrix2, A=row, B=column, C=row_2)

print("--- VALIDATE ---")
if check_matrices(matrix1=matrix1, matrix2=matrix2):
    print("! ok !")
    print("--- MATRIX MULTIPLICATION RESULT ---")
    multiplicate(matrix1=matrix1, matrix2=matrix2)
else:
    print("! entered data is incorrect !")