"""
Лабораторная работа. Вариант 23.
Программа проверки возможности отображения заставки на табло.
"""

def check_cell(ch: str, val: int) -> bool:
    """Проверяет, может ли ячейка табло со значением val отобразить символ ch."""
    if ch == 'R':
        return val in {0, 4, 7}
    if ch == 'G':
        return val in {1, 5, 7}
    if ch == 'B':
        return val in {2, 6, 7}
    if ch == '.':
        return 0 <= val <= 7
    return False

def can_display(splash, board) -> bool:
    """Возвращает True, если заставку можно отобразить на табло."""
    n = len(splash)
    m = len(splash[0])
    for i in range(n):
        for j in range(m):
            if not check_cell(splash[i][j], board[i][j]):
                return False
    return True

def main():
    # Ввод данных
    n, m = map(int, input().split())
    splash = [input().strip() for _ in range(n)]
    board = [list(map(int, input().split())) for _ in range(n)]
    
    # Проверка и вывод
    if can_display(splash, board):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()