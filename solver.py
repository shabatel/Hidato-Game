import datetime

# 9 X 9 MEDIUM
board = [
    [60,59,1,0,6,25,0,18,0],
    [61,58,0,7,4,23,26,16,0],
    [57,62,0,0,0,27,0,20,15],
    [56,54,0,0,28,0,0,11,14],
    [55,0,80,50,30,0,10,0,12],
    [0,0,0,81,0,0,0,0,0],
    [78,0,67,0,0,0,37,33,35],
    [75,72,69,0,48,0,0,0,42],
    [74,0,71,70,0,47,44,40,41]
]

numbers_in_used = [54,1,0,0,1,0,1,1,0,0,
                     1,1,1,0,1,1,1,0,1,
                     0,1,0,0,1,0,1,1,1,
                     1,0,1,0,0,1,0,1,0,
                     1,0,0,1,1,1,0,1,0,
                     0,1,1,0,1,0,0,0,1,
                     1,1,1,1,1,1,1,1,0,
                     0,0,0,1,0,1,1,1,1,
                     0,1,1,0,0,1,0,1,1]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(2, len(board) ** 2):
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


def valid(bo, num, pos):
    if numbers_in_used[num] == 1:
        return False

    num_of_cells = get_num_of_empty_cells(pos[0], pos[1], num)
    if check_if_neighbor_exist(pos[0], pos[1], num - 1):
        if check_if_neighbor_exist(pos[0], pos[1], num + 1):
            return True
        else:
            if num_of_cells > 0 and numbers_in_used[num + 1] == 0:
                return True
            else:
                return False
    else:
        if num_of_cells > 0 and numbers_in_used[num - 1] == 0:
            num_of_cells -= 1
            if check_if_neighbor_exist(pos[0], pos[1], num + 1):
                return True
            elif num_of_cells > 0 and numbers_in_used[num + 1] == 0:
                return True
            else:
                return False
        else:
            return False


def check_if_neighbor_exist(x, y, n):
    for i in range(x - 1, x + 2):
        if 0 <= i < len(board):
            for j in range(y - 1, y + 2):
                if 0 <= j < len(board):
                    if i != x or j != y:
                        if board[i][j] == n:
                            return True
    return False


def get_num_of_empty_cells(x, y, n):
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
            if j % len(board) == 0 and j != 0:
                print(" | ", end="")

            if j == len(board) - 1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    if numbers_in_used[0] != len(board)**2:
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)  # row, col

    return None


print(len(board) ** 2)
print_board(board)
start_time = datetime.datetime.now()
solve(board)
time_delta = datetime.datetime.now() - start_time
print("--------")
print_board(board)
print(time_delta)
