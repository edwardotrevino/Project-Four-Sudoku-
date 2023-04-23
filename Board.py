import pygame
from Cell import Cell



class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_row = None  # The currently selected row
        self.selected_col = None  # The currently selected column
        self.cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)] # create a 2D list of cells to represent the Sudoku board

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
        self.selected_row = row  # Set the selected row to the provided row
        self.selected_col = col  # Set the selected column to the provided column

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
        # clear the value of the selected cell if it is editable
        cell = self.cells[self.selected_row][self.selected_col]
        if cell.editable:
            cell.value = 0
        
    def sketch(self, value):
        # Set the sketched value of the selected cell
        self.cells[self.selected_row][self.selected_col].set_sketched_value(value)

    def place_number(self, value):
        # Set the value of the selected cell
        self.cells[self.selected_row][self.selected_col].value = value

    def reset_to_original(self):
        # reset the board to its original state by clearing all editable cells
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                if cell.editable:
                    cell.value = 0

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False

                # after looping through all the cells, if one of the cells has a value of 0,
                # then the board is not full and this method returns False,
                # if no values are zero, then returns True

        return True

    def update_board(self):
        self.cells = [[Cell([row][col], row, col, self.screen) for col in range(9)] for row in range(9)]

        # updates the board with the new values in each cell after a possible change
        # [row][col] is the value at that position in the underlying 2d board,
        # and that value is passed to the cell corresponding to that row and col

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return (col, row)

                    # when the first cell that contains a value of 0 is found, meaning it is empty,
                    # a tuple of the col (x) and row (y) is returned

    def check_board(self):
        # Check rows for duplicates
        for row in self.cells:
            values = []
            for cell in row:
                if cell.value != 0:
                    values.append(cell.value)
            if len(values) != len(set(values)):
                return False

        # Check columns for duplicates
        for col in range(9):
            values = []
            for row in range(9):
                cell = self.cells[row][col]
                if cell.value != 0:
                    values.append(cell.value)
            if len(values) != len(set(values)):
                return False

        # Check 3x3 boxes for duplicates
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                values = []
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        cell = self.cells[row][col]
                        if cell.value != 0:
                            values.append(cell.value)
                if len(values) != len(set(values)):
                    return False

        return True
