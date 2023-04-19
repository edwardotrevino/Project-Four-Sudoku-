import pygame, sys
from constants import *

pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(MENU_BG_COLOR)


image = pygame.image.load("sudoku_test_img.jpeg")
image = pygame.transform.scale(image, (600, 700))
# adjusts image size to fit screen
screen.blit(image, (0,0))
# only a test image, did not upload to git, if it does not work I can upload the file to git or that line can be deleted

def main_menu():
    main_menu_font = pygame.font.Font(MENU_FONT, MENU_TEXT_SIZE)
    main_menu_text = main_menu_font.render("Welcome to Sudoku", 0, TEXT_COLOR)
    main_menu_surf = main_menu_text.get_rect(center=(300, 150))
    screen.blit(main_menu_text, main_menu_surf)
    # main menu text message "welcome to sudoku"

    game_mode_select_font = pygame.font.Font(MENU_FONT, GAME_MODE_SELECT_SIZE)
    game_mode_select_text = game_mode_select_font.render("Select Game Mode:", 0, TEXT_COLOR)
    game_mode_select_surf = game_mode_select_text.get_rect(center=(300, 350))
    screen.blit(game_mode_select_text, game_mode_select_surf)
    # main menu text message "select game mode:"

    easy_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE)
    easy_button_text = easy_button_font.render("EASY", 0, BUTTON_TEXT_COLOR)
    easy_button_box = pygame.Surface((easy_button_text.get_size()[0] + 5, easy_button_text.get_size()[1] + 5))
    easy_button_box.fill(BUTTON_BG_COLOR)
    easy_button_box.blit(easy_button_text, (2.5, 2.5))
    easy_button_box_rect = easy_button_box.get_rect(center=(150, 475))
    screen.blit(easy_button_box, easy_button_box_rect)

    easy_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(110, 450, 82, 50), 5, 10)
    # creating the easy button design outline

    medium_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE)
    medium_button_text = medium_button_font.render("MEDIUM", 0, BUTTON_TEXT_COLOR)
    medium_button_box = pygame.Surface((medium_button_text.get_size()[0] + 5, medium_button_text.get_size()[1] + 5))
    medium_button_box.fill(BUTTON_BG_COLOR)
    medium_button_box.blit(medium_button_text, (2.5, 2.5))
    medium_button_box_rect = medium_button_box.get_rect(center=(300, 475))
    screen.blit(medium_button_box, medium_button_box_rect)

    medium_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(246, 450, 108, 50), 5, 10)
    # creating the medium button design outline

    hard_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE)
    hard_button_text = hard_button_font.render("HARD", 0, BUTTON_TEXT_COLOR)
    hard_button_box = pygame.Surface((hard_button_text.get_size()[0] + 5, hard_button_text.get_size()[1] + 5))
    hard_button_box.fill(BUTTON_BG_COLOR)
    hard_button_box.blit(hard_button_text, (2.5, 2.5))
    hard_button_box_rect = hard_button_box.get_rect(center=(450, 475))
    screen.blit(hard_button_box, hard_button_box_rect)

    hard_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(408, 450, 85, 50), 5, 10)
    # creating the hard button design outline

while True:
    main_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()



















