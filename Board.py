import pygame
from Cell import Cell



class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        self.cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]

    def draw(self):
        for i in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), ((self.width / 3) * i, 0), ((self.width / 3) * i, self.height), 4)
        # bolded lines delineating vertical lines of 3x3 box
        # self.width and self.height assumed to be 600 each

        for i in range(1, 9):
            if i == 3 or i == 6:
                continue
            pygame.draw.line(self.screen, (0, 0, 0), ((self.width / 9) * i, 0), ((self.width / 9) * i, self.height), 1)
        # vertical thin lines delineating individual cell in 3x3 box

        for i in range(1, 4):
            pygame.draw.line(self.screen, (0, 0, 0), (0, (self.height / 3) * i), (self.width, (self.height / 3) * i), 4)
        # bolded lines delineating horizontal lines of 3x3 box

        for i in range(1, 9):
            if i == 3 or i == 6:
                continue
            pygame.draw.line(self.screen, (0, 0, 0), (0, (self.height / 9) * i), (self.width, (self.height / 9) * i), 1)
        # horizontal thin lines delineating individual cell in 3x3 box

        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()
        # draws cells on the sudoku screen (cell size might be too big for the size of our board in the window)

    def select(self, row, col):
        self.row = row
        self.col = col

    def click(self, x, y):
        if 0 <= x <= 600 and 0 <= y <= 600:

            # if the tuple coordinates from event.pos is in the board, which is 600x600
            # then the below assignment will return the row (x) and col (y) values

            cell_size = 65

            # this variable can be changed or obtained from somewhere else
            # this is the same cell size that is in the draw method of the Cell class
            # the cell_size and cell_padding was summed to give 65

            self.x = self.width // cell_size # if x is 200, then 200 // 65 is 3
            self.y = self.height // cell_size # if y is 300, then 300 // 65 is 4
            return (self.x, self.y) # the return would be (3,4) for example
        return None



    def clear(self):
        pass

    def sketch(self, value):
        self.value = value

    def place_number(self, value):
        self.value = value

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass
