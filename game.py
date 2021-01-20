import time
from solver import valid, set_use

import pygame

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (128,128,128)

# TODO: add grey
pygame.font.init()


class Grid:
    board = [
        [1, 0, 4, 0],
        [2, 13, 0, 7],
        [0, 0, 8, 0],
        [16, 15, 0, 10]
    ]

    def __init__(self, width, height):
        self.rows = len(self.board)
        self.cols = len(self.board)
        self.width = width
        self.height = height
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(self.cols)] for i in range(self.rows)]
        self.selected = None
        self.model = None

    def draw(self, screen):
        # Draw Grid Lines
        gap = self.width / len(self.board)
        for i in range(self.rows + 1):
            thick = 1
            pygame.draw.line(screen, BLACK, (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(screen, BLACK, (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(screen)

    def place(self, val):
        print(val)
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row, col)):
                set_use(val)
                return True
            else:
                self.cubes[row][col].set_tmp(0)
                self.cubes[row][col].set(0)
                self.update_model()
                return False

    def clear(self):
        row, col = self.selected
        # check that the cube is not set value already
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_tmp(0)

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / len(self.board)
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_tmp(val)


class Cube:
    # rows = 9
    # cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.tmp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, screen):
        fnt = pygame.font.SysFont("comicsans", 100)

        gap = self.width / 4
        x = self.col * gap
        y = self.row * gap

        if self.tmp != 0 and self.value == 0:
            text = fnt.render(str(self.tmp), 1, GREY)
            screen.blit(text, (x + 5, y + 5))
        elif not (self.value == 0):
            text = fnt.render(str(self.value), 1, BLACK)
            screen.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(screen, RED, (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_tmp(self, val):
        if self.tmp == 0 or val == 0:
            self.tmp = val
        else:
            self.tmp = (self.tmp * 10) + val


def redraw_screen(screen, board, time1, strikes):
    screen.fill(WHITE)
    # Draw time
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render("Time: " + format_time(time1), 1, BLACK)
    screen.blit(text, (540 - 160, 560))
    # Draw strikers
    text = font.render("X " * strikes, 1, RED)
    screen.blit(text, (20, 560))
    # Draw Grid and board
    board.draw(screen)


def format_time(secs):
    sec = secs % 60
    minute = secs // 60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def main():
    screen = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Hidato")
    board = Grid(540, 540)
    run = True
    key = 8
    strikes = 0
    start = time.time()
    while run:
        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # User using keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_r:
                    # TODO: add 'press r for restart'
                    pygame.quit()
                    pygame.font.init()
                    main()
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    # Try placing the User typing
                    row, col = board.selected
                    if board.cubes[row][col].tmp != 0:
                        if board.place(board.cubes[row][col].tmp):
                            print("Success")
                            if board.is_finished():
                                print("Well Done")
                                run = False
                        else:
                            print("Wrong")
                            board.clear()
                            strikes += 1
                        key = None

            # User using mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.sketch(key)
            key = None

        redraw_screen(screen, board, play_time, strikes)
        pygame.display.update()


main()
pygame.quit()
