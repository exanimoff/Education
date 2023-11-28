n, m = map(int, input().split())

matrix = [[0] * m for _ in range(n)]
num = 1
left, right, top, bottom = 0, m - 1, 0, n - 1

while num <= n * m:
    for j in range(left, right + 1):
        matrix[top][j] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for j in range(right, left - 1, -1):
            matrix[bottom][j] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

# Вывод матрицы с выравниванием
max_length = len(str(n * m))
for row in matrix:
    for num in row:
        print(str(num).ljust(max_length), end=' ')
    print()
