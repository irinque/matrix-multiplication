def multiplicate(matrix1, matrix2, mode):
    matrix1_sorted = list()
    matrix2_sorted = list()

    if mode == 1:
        for line in matrix1:
            matrix1_sorted.append([int(num) for num in line.split()])
        for line in matrix2:
            matrix2_sorted.append([int(num) for num in line.split()])
    elif mode == 2:
        for i in matrix1:
            matrix1_sorted.append(i)
        for i in matrix2:
            matrix2_sorted.append(i)

    result = list()
    for i in range(len(matrix1_sorted)):
        result.append([0 for i in range(len(matrix2_sorted[0]))])

    for i in range(len(matrix1_sorted)):
        for n in range(len(matrix2_sorted[0])):
            for g in range(len(matrix2_sorted)):
                result[i][n] += int(matrix1_sorted[i][g]) * int(matrix2_sorted[g][n])
    
    for matrix_line in result:
        print(*matrix_line)
