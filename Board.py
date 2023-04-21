import pygame


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        pass

    def select(self, row, col):
        self.row = row
        self.col = col

    def click(self, x, y):
        self.x = x
        self.y = y

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
