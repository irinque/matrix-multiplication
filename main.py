import argparse
import random
from data import collect_matrices, output_matrices, validate_dimensions
from multiplication import multiplicate
from generation import generate_matrix


parser = argparse.ArgumentParser(description="select a mode:")
parser.add_argument("-m", '--mode', type=int, help="1 - your matrices\n2 - random matrices", default=1)
args = parser.parse_args()

print("--- MATRICES ---")
if args.mode == 1:
    matrix1, matrix2, dimension_a, dimension_b, dimension_c = collect_matrices()
    output_matrices(matrix1=matrix1, matrix2=matrix2, dimension_a=dimension_a, dimension_b=dimension_b, dimension_c=dimension_c)
elif args.mode == 2:
    dimension_a = random.randint(1, 12)
    dimension_b = random.randint(1, 12)
    dimension_c = random.randint(1, 12)
    matrix1 = generate_matrix(width=dimension_b, height=dimension_a)
    matrix2 = generate_matrix(width=dimension_c, height=dimension_b)
    output_matrices(matrix1=matrix1, matrix2=matrix2, dimension_a=dimension_a, dimension_b=dimension_b, dimension_c=dimension_c)

print("--- VALIDATE ---")
if validate_dimensions(matrix1=matrix1, matrix2=matrix2):
    print("! ok !")
    print("--- MATRIX MULTIPLICATION RESULT ---")
    result = multiplicate(matrix1=matrix1, matrix2=matrix2)
    for matrix_line in result:
        print(*matrix_line)
else:
    print("! entered data is incorrect !")