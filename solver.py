board = [
    [9, 0, 0],
    [0, 4, 1],
    [7, 0, 5]
]

numbers_in_used = [5, 1, 0, 0, 1, 1, 0, 1, 0, 1]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(2, 9):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            numbers_in_used[i] = 1

            if solve(bo):
                return True

            bo[row][col] = 0
            numbers_in_used[i] = 0

    return False


def valid(bo, num, pos):
    return True
    # TODO: check if the insertion is valid


def print_board(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 2:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


print_board(board)