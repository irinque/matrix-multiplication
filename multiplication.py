def multiplicate(matrix1, matrix2):
    if len(matrix2) > len(matrix2):
        m1 = matrix2
        m2 = matrix1
    else:
        m1 = matrix1
        m2 = matrix2
    count = 0
    #       1 2 3
    #       4 5 6
    # 7 8
    # 9 10
    m1_columns = list()
    for i in range(len(m1[0])):
        col = list()
        for line in m1:
            col.append(line[count])
        count += 1
        m1_columns.append(f"{col[0]} {col[1]}")
    for i in range(len(m1)):
        m1_columns.remove("   ")
    print(m1_columns)

    result = list()
        

