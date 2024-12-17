import argparse
import random
import time 
from data import collect_matrices, output_matrices, validate_dimensions, output_result
from multiplication import multiplicate
from generation import generate_matrix


parser = argparse.ArgumentParser(description="select a mode:")
parser.add_argument("-m", '--mode', type=int, help="1 - your matrices\n2 - random matrices\n3 - performance test", default=1)
args = parser.parse_args()

print("--- MATRICES ---")
if args.mode == 1:
    matrix1, matrix2, dimension_a, dimension_b, dimension_c = collect_matrices()
    print(f"first: {dimension_a}x{dimension_b}")
    print(f"second: {dimension_b}x{dimension_c}") 
elif args.mode == 2:
    dimension_a, dimension_b, dimension_c = random.randint(1, 12), random.randint(1, 12), random.randint(1, 12)
    matrix1 = generate_matrix(width=dimension_b, height=dimension_a)
    matrix2 = generate_matrix(width=dimension_c, height=dimension_b)
    print(f"first: {dimension_a}x{dimension_b}")
    print(f"second: {dimension_b}x{dimension_c}") 
    output_matrices(matrix1, matrix2)

elif args.mode == 3:
    dimension = 1000
    matrix1 = generate_matrix(width=dimension, height=dimension)
    matrix2 = generate_matrix(width=dimension, height=dimension)
    print(f"first: {dimension}x{dimension}")
    print(f"second: {dimension}x{dimension}")
    output_matrices(matrix1, matrix2)

print("--- RESULT ---")
if validate_dimensions(matrix1=matrix1, matrix2=matrix2):
    start = time.time()
    result = multiplicate(matrix1=matrix1, matrix2=matrix2)
    finish = time.time()
    print(f"multiplication completed in {round(finish - start, 3)} seconds")
    print(f"- multiplication result in the result.txt file\n- source matrices in matrices.txt")
    output_result(result)
else:
    print("! entered data is incorrect !")