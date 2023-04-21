import pygame
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.font = pygame.font.SysFont(MENU_FONT, 50)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        # Determine the position and size of the cell on the screen
        cell_size = 60
        cell_padding = 10
        cell_x = self.col * cell_size + cell_padding
        cell_y = self.row * cell_size + cell_padding
        cell_rect = pygame.Rect(cell_x, cell_y, cell_size, cell_size)

        # Draw the cell
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), cell_rect, 3)
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), cell_rect, 1)

        # Draw the cell value
        if self.value != 0:
            text = self.font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = cell_rect.center
            self.screen.blit(text, text_rect)
