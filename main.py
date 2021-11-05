import math


def extend(perms, n):
    cells = convert_perms_to_cells(perms, n)
    num_diagonals = get_num_diagonals(cells)
    if num_diagonals == 16:
        print(cells)
        exit()
    elif len(perms) == 15 and num_diagonals < 10:
        return
    elif len(perms) == 25:
        return
    for var in (2, 1, 0):
        perms.append(var)
        cells = convert_perms_to_cells(perms, n)
        row, col = get_row_and_col(perms, n)
        if can_be_extended_to_solution(cells, row, col):
            extend(perms, n)
        perms.pop()


def convert_perms_to_cells(perms, n):
    m = int(math.sqrt(n))
    cells = [[0 for _ in range(m)] for _ in range(m)]
    idx = 0
    for row in range(len(cells)):
        for col in range(len(cells[row])):
            try:
                cells[row][col] = perms[idx]
            except IndexError:
                return cells
            idx += 1
    return cells


def get_num_diagonals(cells):
    count = 0
    for row in cells:
        for value in row:
            if value != 0:
                count += 1
    return count


def can_be_extended_to_solution(cells, row, col):
    diagonal = cells[row][col]
    is_top_safe = True
    is_bottom_safe = True

    if diagonal == 1:
        if row - 1 >= 0 and cells[row - 1][col] == 2:
            is_top_safe = False
        if col - 1 >= 0 and cells[row][col - 1] == 2:
            is_top_safe = False
        if row - 1 >= 0 and col - 1 >= 0 and cells[row - 1][col - 1] == 1:
            is_top_safe = False

    if diagonal == 2:
        if row - 1 >= 0 and cells[row - 1][col] == 1:
            is_top_safe = False
        if row - 1 >= 0 and col + 1 <= len(cells) - 1 and cells[row - 1][col + 1] == 2:
            is_top_safe = False
        if col - 1 >= 0 and cells[row][col - 1] == 1:
            is_bottom_safe = False

    return is_top_safe and is_bottom_safe


def get_row_and_col(perms, n):
    if len(perms) % int(math.sqrt(n)) == 0:
        row = len(perms) // int(math.sqrt(n)) - 1
        col = int(math.sqrt(n)) - 1
    else:
        row = len(perms) // int(math.sqrt(n))
        col = len(perms) % int(math.sqrt(n)) - 1
    return row, col


extend(perms=[], n=25)