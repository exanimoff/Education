"""
Создаём доску 12x12, чтобы избежать выхода за границы матрицы при расстановке "*"
заполняем доску соответствующими названиями клеток
в клетке с нужным названием располагаем коня
все названия клеток меняем на "." и расставляем "*" по координатам
"""
N = input()
target = '*'
matrix = []
a = 'ZZabcdefghZZ'
nums = 'ZZ87654321ZZ'
for j in range(12):
    row = []
    for i in range(12):
        row.append((str(list(a)[i]) + str(list(nums)[j])))
    matrix.append(row)
for i in range(12):
    for j in range(12):
        if matrix[i][j] == N:
            matrix[i][j] = 'N'
        else:
            matrix[i][j] = '.'
for i in range(12):
    for j in range(12):
        if matrix[i][j] == 'N':
            matrix[i - 2][j-1] = target
            matrix[i - 1][j - 2] = target
            matrix[i - 2][j + 1] = target
            matrix[i - 1][j + 2] = target
            matrix[i + 2][j + 1] = target
            matrix[i + 1][j + 2] = target
            matrix[i + 2][j - 1] = target
            matrix[i + 1][j - 2] = target
for i in range(2,10):
    for j in range(2,10):
        print(matrix[i][j], end=' ')
    print()