import math, random


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = 9
        self.removed_cells = removed_cells
        self.box_length = 3
        self.board = [["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["-", "-", "-", "-", "-", "-", "-", "-", "-"]]

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:  # iterate over each row in the board
            for col in row:  # iterate over each column in the current row
                print(col, end=" ")  # print the current cell, followed by a space
            print()  # move to the next line after each row has been printed

    def valid_in_row(self, row, num):  # row = self.get_board[row#]
        if num in self.get_board()[row]:
            return False
        return True

    def valid_in_col(self, col, num):  # for loop to iterate through each value of row, then col = self.get_board[row(i)][col(input)]
        for row in range(len(self.get_board())):
            if num is self.get_board()[row][col]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        # not completely sure of application
        if 0 <= row_start <= 2:
            row_start = 0
        elif 3 <= row_start <= 5:
            row_start = 3
        elif 6 <= row_start <= 8:
            row_start = 6

        # based on row_start information, the row_start is adjusted so that the row_start variable
        # starts at the first row of each of the 9 3x3 boxes of the Sudoku board, so that a repeated number
        # can be checked only in a fixed 3x3 box of the Sudoku board
        # row indices 0-2 are the first row of 3x3 boxes, 3-5 are the second row of 3x3 boxes, and 6-8 are the third row

        if 0 <= col_start <= 2:
            col_start = 0
        elif 3 <= col_start <= 5:
            col_start = 3
        elif 6 <= col_start <= 8:
            col_start = 6
        

        # similar to above, the row_start and col_start are adjusted to start at the first row and col of each 3x3 box
        # ex: row_start of 4 and col_start of 3 corresponds to the middle 3x3 box on board and to iterate through it
        # row_start and col_start are changed so row_start = 3 and col_start = 3 (end would be end of box at 5, 5)

        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.get_board()[row][col] == num:
                    return False
        return True

        # loops through rows from the specified row_start to row_start + 2
        # and cols from col_start to col_start + 2, to determine if num is in a given 3x3 box
        # row_start + 3 and col_start + 3 because end number in range func. is not inclusive

    def is_valid(self, row, col, num):
        if self.valid_in_box(row, col, num) and self.valid_in_row(row, num) and self.valid_in_col(col, num):
            return True
        return False

        # if the num is already in the 3x3 box or the specified row or col; then is_valid returns False, if not, is_valid returns True
        # not sure if this method should return false if user tries to change randomly generated numbers
        # or if that is determined in a different method, if not this should work

     

    def fill_box(self, row_start, col_start):
        # Adjust row_start to the first row of the corresponding 3x3 box
        if 0 <= row_start <= 2:
            row_start = 0
        elif 3 <= row_start <= 5:
            row_start = 3
        elif 6 <= row_start <= 8:
            row_start = 6

        # Adjust col_start to the first column of the corresponding 3x3 box
        if 0 <= col_start <= 2:
            col_start = 0
        elif 3 <= col_start <= 5:
            col_start = 3
        elif 6 <= col_start <= 8:
            col_start = 6

        box_values = list(range(1, 10))  # Create a list of the numbers 1 to 9
        random.shuffle(box_values)  # Shuffle the list to get a random order of the numbers

        # Loop through each cell in the 3x3 box and assign a value
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                value = box_values.pop()  # Get the last value from the shuffled list and remove it
                self.get_board()[row][col] = value  # Assign the value to the cell

    def fill_diagonal(self):
        diagonal_box_indices = [0, 3, 6]
        for i in diagonal_box_indices:
            self.fill_box(i,i)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

    Parameters:
    row, col specify the coordinates of the first empty (0) cell
    Return:
    boolean (whether or not we could solve the board)
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining
    Parameters: None
    Return: None
    '''

    def remove_cells(self):
    # Get the number of cells to remove
    cells_to_remove = self.removed_cells
    # Loop until the desired number of cells have been removed
    while cells_to_remove > 0:
        # Get a random row and column
        row = random.randint(0, self.row_length - 1)
        col = random.randint(0, self.row_length - 1)
        # If the cell is not already empty
        if self.get_board()[row][col] != 0:
            # Remove the cell by setting its value to 0
            self.get_board()[row][col] = 0
            # Decrease the count of cells to remove
            cells_to_remove -= 1

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution
Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)
Return: list[list] (a 2D Python list to represent the board)
'''




