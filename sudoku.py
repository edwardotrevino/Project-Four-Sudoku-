
class SudokuGenerator:

    def __init__(self, removed_cells):
        self.row_length = 9
        self.removed_cells = removed_cells

    def get_board(self):
        return [["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-", "-", "-"]]

    def print_board(self):
        for row in self.get_board()[0]:  # row: ["-", "-", "-", "-", "-", "-","-", "-", "-"]
            for col in self.get_board()[0]:
                print(col, end=" ")
            print()

    def valid_in_row(self, row, num):  # row = self.get_board[row#]
        if num in self.get_board()[row]:
            return False
        return True

    def valid_in_col(self, col, num):  # for loop to iterate through each value of row, then col = self.get_board[row(i)][col(input)]
        for row in range(len(self.get_board())):
            if num in self.get_board()[row][col]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        pass

    def is_valid(self, row, col, num):
        pass

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        pass

    def fill_remaining(self, row, col):
        pass

    def fill_values(self):
        pass

    def remove_cells(self):
        pass

    def generate_sudoku(size, removed):
        pass




