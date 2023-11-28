"""
Это решение использует функции для создания доски, проверки позиции, обозначения ходов коня и вывода доски на экран.
Оно является более модульным, понятным и поддерживаемым.
Также оно корректно работает с вводом координат в шахматной нотации.
"""
def create_chessboard():
    # Создаем шахматную доску 8x8 и заполняем ее точками
    return [['.' for _ in range(8)] for _ in range(8)]

def is_valid_position(row, col):
    # Проверяем, находится ли клетка в пределах доски
    return 0 <= row < 8 and 0 <= col < 8

def mark_knight_moves(board, row, col):
    # Отмечаем положение коня и его возможные ходы на доске
    board[row][col] = 'N'
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if is_valid_position(new_row, new_col):
            board[new_row][new_col] = '*'

def print_chessboard(board):
    # Выводим доску на экран
    for row in board:
        print(' '.join(row))

# Ввод координат коня
coordinates = input()
col = ord(coordinates[0]) - ord('a')
row = 8 - int(coordinates[1])

# Создание и обозначение доски
chessboard = create_chessboard()
mark_knight_moves(chessboard, row, col)

# Вывод доски на экран
print_chessboard(chessboard)
