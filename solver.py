import datetime

# board = [
#     [1, 0, 4, 0],
#     [2, 13, 0, 7],
#     [0, 0, 8, 0],
#     [16, 15, 0, 10]
# ]

numbers_in_used = [9, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(2, len(bo) ** 2):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            numbers_in_used[i] = 1
            numbers_in_used[0] += 1

            if solve(bo):
                return True

            bo[row][col] = 0
            numbers_in_used[i] = 0
            numbers_in_used[0] -= 1

    return False


def set_use(num):
    numbers_in_used[num] = 1


def valid(bo, num, pos):
    if numbers_in_used[num] == 1:
        return False

    num_of_cells = get_num_of_empty_cells(bo, pos[0], pos[1], num)
    if check_if_neighbor_exist(bo, pos[0], pos[1], num - 1):
        if check_if_neighbor_exist(bo, pos[0], pos[1], num + 1):
            return True
        else:
            if num_of_cells > 0 and numbers_in_used[num + 1] == 0:
                return True
            else:
                return False
    else:
        if num_of_cells > 0 and numbers_in_used[num - 1] == 0:
            num_of_cells -= 1
            if check_if_neighbor_exist(bo, pos[0], pos[1], num + 1):
                return True
            elif num_of_cells > 0 and numbers_in_used[num + 1] == 0:
                return True
            else:
                return False
        else:
            return False


def check_if_neighbor_exist(bo, x, y, n):
    for i in range(x - 1, x + 2):
        if 0 <= i < len(bo):
            for j in range(y - 1, y + 2):
                if 0 <= j < len(bo):
                    if i != x or j != y:
                        if bo[i][j] == n:
                            return True
    return False


def get_num_of_empty_cells(bo, x, y, n):
    empty_cells = 0
    for i in range(x - 1, x + 2):
        if 0 <= i < len(bo):
            for j in range(y - 1, y + 2):
                if 0 <= j < len(bo):
                    if i != x or j != y:
                        if bo[i][j] == 0:
                            empty_cells += 1
    return empty_cells


def print_board(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if j == len(bo) - 1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    if numbers_in_used[0] != len(bo) ** 2:
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)  # row, col

    return None

########### take out the comments in order to solve it by itself#######
# print_board(board)
# solve(board)
# print("--------")
# print_board(board)
