import pygame, sys
from SudokuGenerator import SudokuGenerator, generate_sudoku
from Board import Board
from Cell import Cell
from constants import *


pygame.init()
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(MENU_BG_COLOR)

image = pygame.image.load("sudoku_test_img.jpeg")
image = pygame.transform.scale(image, (600, 700))
screen.blit(image, (0, 0))

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
    outer_rect_2 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(246, 450, 108, 50), 2)
    inner_rect_2 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(250, 455, 100, 40), 2)
    # creating the medium button design outline

    hard_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE)
    hard_button_text = hard_button_font.render("HARD", 0, BUTTON_TEXT_COLOR)
    hard_button_box = pygame.Surface((hard_button_text.get_size()[0] + 5, hard_button_text.get_size()[1] + 5))
    hard_button_box.fill(BUTTON_BG_COLOR)
    hard_button_box.blit(hard_button_text, (2.5, 2.5))
    hard_button_box_rect = hard_button_box.get_rect(center=(450, 475))
    screen.blit(hard_button_box, hard_button_box_rect)

    hard_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(408, 450, 85, 50), 5)
    outer_rect_3 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(408, 450, 85, 50), 2)
    inner_rect_3 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(413, 455, 75, 40), 2)
    # creating the hard button design outline
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button_rect.collidepoint(event.pos):
                    removed = 30
                    return removed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if medium_button_rect.collidepoint(event.pos):
                    removed = 40
                    return removed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hard_button_rect.collidepoint(event.pos):
                    removed = 50
                    return removed

        pygame.display.update()


main_menu()
removed = main_menu()
if __name__ == "__main__":
    screen.fill(GAME_BG_COLOR)  # active-game background
    easy_sudoku = generate_sudoku(9, removed)  # generates sudoku board with 30 removed cells
    easy_board = Board(WIDTH, HEIGHT - 100, screen, "easy", easy_sudoku)
    removed = 30
    difficulty = "easy"
    sudoku = easy_sudoku
    board = easy_board
    easy_board.draw()

    game_restart_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE + 5)
    game_restart_button_text = game_restart_button_font.render("RESTART", 0, BUTTON_TEXT_COLOR)
    game_restart_button_box = pygame.Surface(
        (game_restart_button_text.get_size()[0] + 5, game_restart_button_text.get_size()[1] + 5))
    game_restart_button_box.fill(BUTTON_BG_COLOR)
    game_restart_button_box.blit(game_restart_button_text, (2.5, 2.5))
    game_restart_button_box_rect = game_restart_button_box.get_rect(center=(305, 650))

    game_exit_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE + 5)
    game_exit_button_text = game_exit_button_font.render("EXIT", 0, BUTTON_TEXT_COLOR)
    game_exit_button_box = pygame.Surface(
        (game_exit_button_text.get_size()[0] + 5, game_exit_button_text.get_size()[1] + 5))
    game_exit_button_box.fill(BUTTON_BG_COLOR)
    game_exit_button_box.blit(game_exit_button_text, (2.5, 2.5))
    game_exit_button_box_rect = game_exit_button_box.get_rect(center=(480, 650))

    game_reset_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE + 5)
    game_reset_button_text = game_reset_button_font.render("RESET", 0, BUTTON_TEXT_COLOR)
    game_reset_button_box = pygame.Surface(
        (game_reset_button_text.get_size()[0] + 5, game_reset_button_text.get_size()[1] + 5))
    game_reset_button_box.fill(BUTTON_BG_COLOR)
    game_reset_button_box.blit(game_reset_button_text, (2.5, 2.5))
    game_reset_button_box_rect = game_reset_button_box.get_rect(center=(120, 650))

    screen.blit(game_restart_button_box, game_restart_button_box_rect)
    game_restart_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(238, 625, 135, 50), 5)
    game_outer_rect_1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(238, 625, 135, 50), 2)
    game_inner_rect_1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(243, 630, 125, 40), 2)
    # restart button blit onto screen

    screen.blit(game_exit_button_box, game_exit_button_box_rect)
    game_exit_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(438, 625, 85, 50), 5)
    game_outer_rect_2 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(438, 625, 85, 50), 2)
    game_inner_rect_2 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(443, 630, 75, 40), 2)
    # exit button blit onto screen

    screen.blit(game_reset_button_box, game_reset_button_box_rect)
    game_reset_button_rect = pygame.draw.rect(screen, RECTANGLE_COLOR, pygame.Rect(68, 625, 106, 50), 5)
    game_outer_rect_3 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(68, 625, 106, 50), 2)
    game_inner_rect_3 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(73, 630, 96, 40), 2)
    # reset button blit onto screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if board.click(x, y) != None:
                    selected_x, selected_y = board.click(x, y)
                    board.select(selected_x, selected_y)
                if game_reset_button_rect.collidepoint(event.pos):
                    screen.fill((255, 0, 0))
                if game_restart_button_rect.collidepoint(event.pos):
                    screen.fill((255, 0, 0))
                if game_exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    value = 1
                if event.key == pygame.K_2:
                    value = 2
                if event.key == pygame.K_3:
                    value = 3
                if event.key == pygame.K_4:
                    value = 4
                if event.key == pygame.K_5:
                    value = 5
                if event.key == pygame.K_6:
                    value = 6
                if event.key == pygame.K_7:
                    value = 7
                if event.key == pygame.K_8:
                    value = 8
                if event.key == pygame.K_9:
                    value = 9
                board.sketch(value)
                board.draw()
                if event.key == pygame.K_RETURN:
                    board.place_number(value)
                    board.draw()
            if board.is_full():
                if board.check_board():
                    screen.fill((0,0,0))


        pygame.display.update()