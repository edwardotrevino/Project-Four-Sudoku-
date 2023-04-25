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

game_restart_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE + 5)
game_restart_button_text = game_restart_button_font.render("RESTART", 0, BUTTON_TEXT_COLOR)
game_restart_button_box = pygame.Surface((game_restart_button_text.get_size()[0] + 5, game_restart_button_text.get_size()[1] + 5))
game_restart_button_box.fill(BUTTON_BG_COLOR)
game_restart_button_box.blit(game_restart_button_text, (2.5, 2.5))
game_restart_button_box_rect = game_restart_button_box.get_rect(center=(305, 650))

game_exit_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE + 5)
game_exit_button_text = game_exit_button_font.render("EXIT", 0, BUTTON_TEXT_COLOR)
game_exit_button_box = pygame.Surface((game_exit_button_text.get_size()[0] + 5, game_exit_button_text.get_size()[1] + 5))
game_exit_button_box.fill(BUTTON_BG_COLOR)
game_exit_button_box.blit(game_exit_button_text, (2.5, 2.5))
game_exit_button_box_rect = game_exit_button_box.get_rect(center=(480, 650))

game_reset_button_font = pygame.font.Font(BUTTON_TEXT_FONT, BUTTON_TEXT_SIZE + 5)
game_reset_button_text = game_reset_button_font.render("RESET", 0, BUTTON_TEXT_COLOR)
game_reset_button_box = pygame.Surface((game_reset_button_text.get_size()[0] + 5, game_reset_button_text.get_size()[1] + 5))
game_reset_button_box.fill(BUTTON_BG_COLOR)
game_reset_button_box.blit(game_reset_button_text, (2.5, 2.5))
game_reset_button_box_rect = game_reset_button_box.get_rect(center=(120, 650))

def main_menu():
    main_menu_font = pygame.font.Font(MENU_FONT, MENU_TEXT_SIZE)
    main_menu_text = main_menu_font.render("Welcome to Sudoku", 0, TEXT_COLOR)
    main_menu_surf = main_menu_text.get_rect(center=(300, 150))
    screen.blit(main_menu_text, main_menu_surf)
    # main menu text message "welcome to sudoku"

def game_mode_select():
    game_mode_select_font = pygame.font.Font(MENU_FONT, GAME_MODE_SELECT_SIZE)
    game_mode_select_text = game_mode_select_font.render("Select Game Mode:", 0, TEXT_COLOR)
    game_mode_select_surf = game_mode_select_text.get_rect(center=(300, 350))
    screen.blit(game_mode_select_text, game_mode_select_surf)
    # main menu text message "select game mode:"

def reset_restart_exit_code():
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

    if game_restart_button_rect.collidepoint(event.pos):
        screen.fill(GAME_BG_COLOR)  # active-game
        sudoku = generate_sudoku(9, removed)  # generates sudoku board with 30 removed cells
        board = Board(WIDTH, HEIGHT - 100, screen, difficulty, sudoku)
        board.draw()  # draws sudoku board on the screen

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

    if game_exit_button_rect.collidepoint(event.pos):
        pygame.quit()
        sys.exit()

    if game_reset_button_rect.collidepoint(event.pos):
        board.reset_to_original()  # (temp solution) can't be completely sure this works until testing it with player changes to the board
        board.draw()  # draws sudoku board on the screen

main_menu()
game_mode_select()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy_button_rect.collidepoint(event.pos): # this is the response to pressing the easy button
                screen.fill(GAME_BG_COLOR) # active-game background
                easy_sudoku = generate_sudoku(9, 30) # generates sudoku board with 30 removed cells
                easy_board = Board(WIDTH, HEIGHT - 100, screen, "easy", easy_sudoku)
                removed = 30
                difficulty = "easy"
                sudoku = easy_sudoku
                board = easy_board
                easy_board.draw() # draws sudoku board on the screen
                # this is just the minimum code so that the board can show up on the screen

            if medium_button_rect.collidepoint(event.pos):  # this is the response to pressing the medium button
                screen.fill(GAME_BG_COLOR)  # active-game background
                medium_sudoku = generate_sudoku(9, 40)  # generates sudoku board with 30 removed cells
                medium_board = Board(WIDTH, HEIGHT - 100, screen, "medium", medium_sudoku)
                removed = 40
                difficulty = "medium"
                sudoku = medium_sudoku
                board = medium_board
                medium_board.draw()  # draws sudoku board on the screen
                # this is just the minimum code so that the board can show up on the screen

            if hard_button_rect.collidepoint(event.pos):  # this is the response to pressing the hard button
                screen.fill(GAME_BG_COLOR)  # active-game background
                hard_sudoku = generate_sudoku(9, 50)  # generates sudoku board with 30 removed cells
                hard_board = Board(WIDTH, HEIGHT - 100, screen, "hard", hard_sudoku)
                removed = 50
                difficulty = "hard"
                sudoku = hard_sudoku
                board = hard_board
                hard_board.draw()  # draws sudoku board on the screen
                # this is just the minimum code so that the board can show up on the screen

            reset_restart_exit_code()  # function containing the code for each in-game button; reset, restart, and exit

        if event.type == pygame.MOUSEBUTTONDOWN:  # *very experimental from here on*
            x, y = event.pos                      # defines the x and y coordinates for passing into the board.click function
            if board.click(x, y) is None:
                pass
            else:
                board.select(board.row, board.col)  # selects the cell that board.click returns
        elif event.type == pygame.KEYDOWN:     # very experimental keyboard input logic
            if event.key == pygame.K_1:
                key = 1
            elif event.key == pygame.K_2:
                key = 2
            elif event.key == pygame.K_3:
                key = 3
            elif event.key == pygame.K_4:
                key = 4
            elif event.key == pygame.K_5:       # will set "key" equal to whatever value key on the keyboard is pressed
                key = 5
            elif event.key == pygame.K_6:
                key = 6
            elif event.key == pygame.K_7:
                key = 7
            elif event.key == pygame.K_8:
                key = 8
            elif event.key == pygame.K_9:
                key = 9
            else:
                key = 0
            board.place_number(key)             # places the correct value of the key pressed onto the board, in the selected cell
            if board.check_board():             # checks whether or not the board is valid before drawing the changes
                board.draw()
            else:
                screen.fill(GAME_BG_COLOR)      # make shift "you lost" screen appears if check_board returns false
                main_menu_font = pygame.font.Font(MENU_FONT, MENU_TEXT_SIZE)
                main_menu_text = main_menu_font.render("YOU LOSE", 0, TEXT_COLOR)
                main_menu_surf = main_menu_text.get_rect(center=(300, 150))
                screen.blit(main_menu_text, main_menu_surf)
            if board.is_full():
                screen.fill(GAME_BG_COLOR)  # make shift "you win" screen appears if is_full returns true
                main_menu_font = pygame.font.Font(MENU_FONT, MENU_TEXT_SIZE)
                main_menu_text = main_menu_font.render("YOU WIN", 0, TEXT_COLOR)
                main_menu_surf = main_menu_text.get_rect(center=(300, 150))
                screen.blit(main_menu_text, main_menu_surf)
    pygame.display.update()

