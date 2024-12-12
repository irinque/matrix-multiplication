import argparse
import random
from data import collect_matrices, output_matrices, check_matrices
from multiplication import multiplicate
from generation import generate_matrix


#question = int(input("select a mode:\n1 - your matrices\n2 - generate random matrices\n3 - generate random matrices\n! enter only a number !\n"))
parser = argparse.ArgumentParser(description="select a mode:")
parser.add_argument("mode", type=int, help="1 - your matrices from file\n2 - generate random matrices")
args = parser.parse_args()

if args.mode == 1:
    matrix1, matrix2 = collect_matrices()

elif args.mode == 2:
    A = random.randint(1, 7)
    B = random.randint(1, 7)
    C = random.randint(1, 7)
    matrix1 = generate_matrix(width=B, height=A)
    matrix2 = generate_matrix(width=C, height=B)

print("--- MATRICES ---")
output_matrices(matrix1=matrix1, matrix2=matrix2)

print("--- VALIDATE ---")
if check_matrices(matrix1=matrix1, matrix2=matrix2):
    print("! ok !")
    print("--- MATRIX MULTIPLICATION RESULT ---")
    multiplicate(matrix1=matrix1, matrix2=matrix2)
else:
    print("! entered data is incorrect !")