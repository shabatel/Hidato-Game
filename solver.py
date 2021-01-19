# import datetime

numbers_in_used = [5, 1, 0, 0, 1, 1, 0, 1, 0, 1]


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(2, len(board) ** 2):
        if valid(board, i, (row, col)):
            board[row][col] = i
            numbers_in_used[i] = 1
            numbers_in_used[0] += 1

            if solve(board):
                return True

            board[row][col] = 0
            numbers_in_used[i] = 0
            numbers_in_used[0] -= 1

    return False


def valid(board, num, pos):
    if numbers_in_used[num] == 1:
        return False

    num_of_cells = get_num_of_empty_cells(board, pos[0], pos[1], num)
    if check_if_neighbor_exist(board, pos[0], pos[1], num - 1):
        if check_if_neighbor_exist(board, pos[0], pos[1], num + 1):
            return True
        else:
            if num_of_cells > 0 and numbers_in_used[num + 1] == 0:
                return True
            else:
                return False
    else:
        if num_of_cells > 0 and numbers_in_used[num - 1] == 0:
            num_of_cells -= 1
            if check_if_neighbor_exist(board, pos[0], pos[1], num + 1):
                return True
            elif num_of_cells > 0 and numbers_in_used[num + 1] == 0:
                return True
            else:
                return False
        else:
            return False


def check_if_neighbor_exist(board, x, y, n):
    for i in range(x - 1, x + 2):
        if 0 <= i < len(board):
            for j in range(y - 1, y + 2):
                if 0 <= j < len(board):
                    if i != x or j != y:
                        if board[i][j] == n:
                            return True
    return False


def get_num_of_empty_cells(board, x, y, n):
    empty_cells = 0
    for i in range(x - 1, x + 2):
        if 0 <= i < len(board):
            for j in range(y - 1, y + 2):
                if 0 <= j < len(board):
                    if i != x or j != y:
                        if board[i][j] == 0:
                            empty_cells += 1
    return empty_cells


def print_board(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if j % len(bo) == 0 and j != 0:
                print(" | ", end="")

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

# print(len(board) ** 2)
# print_board(board)
# start_time = datetime.datetime.now()
# solve(board)
# time_delta = datetime.datetime.now() - start_time
# print("--------")
# print_board(board)
# print(time_delta)
