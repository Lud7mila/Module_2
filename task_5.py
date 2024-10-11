def get_matrix(n, m, value):
    matrix = []

    if n <= 0 or m <= 0:
        return matrix

    for row in range(n):
        matrix.append([])
        for column in range(m):
            matrix[row].append(value)

    return matrix

row_count = input("Введите количество строк: ")
column_count = input("Введите количество столбцов: ")
value = input("Введите значение элемента матрицы: ")

result_matrix = get_matrix(int(row_count), int(column_count), int(value))
print(result_matrix)