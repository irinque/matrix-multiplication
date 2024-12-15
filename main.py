import argparse
import random
from data import collect_matrices, output_matrices, validate_dimensions
from multiplication import multiplicate
from generation import generate_matrix


parser = argparse.ArgumentParser(description="select a mode:")
parser.add_argument("-m", '--mode', type=int, help="1 - your matrices\n2 - random matrices\n3 - performance test", default=1)
args = parser.parse_args()

print("--- MATRICES ---")
if args.mode == 1:
    matrix1, matrix2, dimension_a, dimension_b, dimension_c = collect_matrices()
    print(f"first: {dimension_a}x{dimension_b}")
    output_matrices(matrix=matrix1)
    print(f"second: {dimension_b}x{dimension_c}") 
    output_matrices(matrix=matrix2)
elif args.mode == 2:
    dimension_a, dimension_b, dimension_c = random.randint(1, 12), random.randint(1, 12), random.randint(1, 12)
    matrix1, runtime_generation1 = generate_matrix(width=dimension_b, height=dimension_a)
    matrix2, runtime_generation2 = generate_matrix(width=dimension_c, height=dimension_b)
    print(f"first: {dimension_a}x{dimension_b}")
    output_matrices(matrix=matrix1)
    print(f"second: {dimension_b}x{dimension_c}") 
    output_matrices(matrix=matrix2)

elif args.mode == 3:
    dimension = 10000
    matrix1, runtime_generation1 = generate_matrix(width=dimension, height=dimension)
    matrix2, runtime_generation2 = generate_matrix(width=dimension, height=dimension)
    print(f"first: {dimension}x{dimension}")
    print(f"second: {dimension}x{dimension}")

print("--- VALIDATE ---")
if validate_dimensions(matrix1=matrix1, matrix2=matrix2):
    print("! ok !")
    print("--- MATRIX MULTIPLICATION RESULT ---")
    result, runtime_multiplication = multiplicate(matrix1=matrix1, matrix2=matrix2)
    for matrix_line in result:
        print(*matrix_line)
    print(f"--- STATS ---\n\nmatrix1({dimension_a}x{dimension_b}) generated for: {runtime_generation1}\nmatrix2({dimension_b}x{dimension_c}) generated for: {runtime_generation2}\nmultiplication ended for: {runtime_multiplication}")
else:
    print("! entered data is incorrect !")