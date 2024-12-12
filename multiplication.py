def multiplicate(matrix1, matrix2):
    matrix1_sorted = list()
    matrix2_sorted = list()

    for line in matrix1:
        matrix1_sorted.append(line)
    for line in matrix2:
        matrix2_sorted.append(line)

    result = list()
    for i in range(len(matrix1_sorted)):
        result.append([0 for i in range(len(matrix2_sorted[0]))])

    for i in range(len(matrix1_sorted)):
        for n in range(len(matrix2_sorted[0])):
            for g in range(len(matrix2_sorted)):
                result[i][n] += int(matrix1_sorted[i][g]) * int(matrix2_sorted[g][n])
    
    for matrix_line in result:
        print(*matrix_line)
