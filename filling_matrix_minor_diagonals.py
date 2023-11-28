def fill_diagonals(row, col):
    matrix = [[0 for _ in range(col)] for _ in range(row)]
    value = 1

    for d in range(row + col - 1):
        if d < col:
            i = 0
            j = d
        else:
            i = d - col + 1
            j = col - 1

        while j >= 0 and i < row:
            matrix[i][j] = value
            value += 1
            i += 1
            j -= 1

    return matrix

n, m = map(int, input().split())
result = fill_diagonals(n, m)
for rows in result:
    print(*rows)
