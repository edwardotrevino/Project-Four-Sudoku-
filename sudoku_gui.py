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

    easy_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(110, 450, 82, 50), 5)
    outer_rect_1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(110, 450, 82, 50), 2)
    inner_rect_1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(115, 455, 72, 40), 2)
    # creating the easy button design outline

    medium_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE)
    medium_button_text = medium_button_font.render("MEDIUM", 0, BUTTON_TEXT_COLOR)
    medium_button_box = pygame.Surface((medium_button_text.get_size()[0] + 5, medium_button_text.get_size()[1] + 5))
    medium_button_box.fill(BUTTON_BG_COLOR)
    medium_button_box.blit(medium_button_text, (2.5, 2.5))
    medium_button_box_rect = medium_button_box.get_rect(center=(300, 475))
    screen.blit(medium_button_box, medium_button_box_rect)

    medium_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(246, 450, 108, 50), 5)
    outer_rect_2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(246, 450, 108, 50), 2)
    inner_rect_2 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(250, 455, 100, 40), 2)
    # creating the medium button design outline

    hard_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE)
    hard_button_text = hard_button_font.render("HARD", 0, BUTTON_TEXT_COLOR)
    hard_button_box = pygame.Surface((hard_button_text.get_size()[0] + 5, hard_button_text.get_size()[1] + 5))
    hard_button_box.fill(BUTTON_BG_COLOR)
    hard_button_box.blit(hard_button_text, (2.5, 2.5))
    hard_button_box_rect = hard_button_box.get_rect(center=(450, 475))
    screen.blit(hard_button_box, hard_button_box_rect)

    hard_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(408, 450, 85, 50), 5)
    outer_rect_3 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(408, 450, 85, 50), 2)
    inner_rect_3 = pygame.draw.rect(screen, (0,0,0), pygame.Rect(413, 455, 75, 40), 2)
    # creating the hard button design outline



    temp_font = pygame.font.Font(MENU_FONT, 35)
    temp_text = temp_font.render("Press 1 to view game won screen outline...", 0, TEXT_COLOR)
    temp_text_surf = temp_text.get_rect(center=(300, 550))
    screen.blit(temp_text, temp_text_surf)
    temp_font2 = pygame.font.Font(MENU_FONT, 35)
    temp_text2 = temp_font2.render("Press 2 to view game lost screen outline..", 0, TEXT_COLOR)
    temp_text_surf2 = temp_text2.get_rect(center=(300, 600))
    screen.blit(temp_text2, temp_text_surf2)
    # this is temporary code so the game won and game over screen outlines can be viewed

def game_over():
    # the game won screen is displayed if player wins and
    # the game lost screen is displayed if player loses
    # game won variable is temporary and can be changed later, created so the screens can be viewed
    if game_won:
        screen.fill(MENU_BG_COLOR)
        game_won_font = pygame.font.Font(MENU_FONT, MENU_TEXT_SIZE)
        game_won_text = game_won_font.render("Game Won!", 0, TEXT_COLOR)
        game_won_surf = game_won_text.get_rect(center=(300, 200))
        screen.blit(game_won_text, game_won_surf)

        restart_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE + 5)
        restart_button_text = restart_button_font.render("RESTART", 0, BUTTON_TEXT_COLOR)
        restart_button_box = pygame.Surface((restart_button_text.get_size()[0] + 5, restart_button_text.get_size()[1] + 5))
        restart_button_box.fill(BUTTON_BG_COLOR)
        restart_button_box.blit(restart_button_text, (2.5, 2.5))
        restart_button_box_rect = restart_button_box.get_rect(center=(300, 375))
        screen.blit(restart_button_box, restart_button_box_rect)

        restart_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(230, 350, 140, 50), 5)
        outer_rect_1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(230, 350, 140, 50), 2)
        inner_rect_1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(235, 355, 130, 40), 2)

        # outline for the game won screen

    else:
        screen.fill(MENU_BG_COLOR)
        game_lost_font = pygame.font.Font(MENU_FONT, MENU_TEXT_SIZE)
        game_lost_text = game_lost_font.render("Game Over :(", 0, TEXT_COLOR)
        game_lost_surf = game_lost_text.get_rect(center=(300, 200))
        screen.blit(game_lost_text, game_lost_surf)

        exit_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE + 5)
        exit_button_text = exit_button_font.render("EXIT", 0, BUTTON_TEXT_COLOR)
        exit_button_box = pygame.Surface((exit_button_text.get_size()[0] + 5, exit_button_text.get_size()[1] + 5))
        exit_button_box.fill(BUTTON_BG_COLOR)
        exit_button_box.blit(exit_button_text, (2.5, 2.5))
        exit_button_box_rect = exit_button_box.get_rect(center=(300, 375))
        screen.blit(exit_button_box, exit_button_box_rect)

        exit_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(254, 350, 95, 50), 5)
        outer_rect_2 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(254, 350, 95, 50), 2)
        inner_rect_2 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(259, 355, 85, 40), 2)

        # outline for the game lost screen



main_menu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                game_won = True
                game_over()
            if event.key == pygame.K_2:
                game_won = False
                game_over()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            # this code is for the functionality

    pygame.display.update()



















