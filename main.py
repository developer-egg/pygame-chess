import sys

import pygame

pygame.init()

SCREEN_HEIGHT = 1024
SCREEN_WIDTH = 1024

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess Game")

board = [[None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None]]

running = True


def draw_squares():
    square_count = 0
    square_count_color_ref = 0
    total_squares = 64

    x_offset = 0
    y_offset = 0

    green = (118, 150, 86)
    white = (238, 238, 210)

    current_row_index = 0
    current_col_index = 0

    current_color = white

    for count in range(total_squares):
        if square_count_color_ref % 2 == 0:
            current_color = white
        else:
            current_color = green

        # this may be a problem later because the board gets reset every pass of the game loop first index is the
        # square, second index is the coordinates of the top-left corner, third index is the coordinates of the
        # bottom-left corner
        board[current_row_index][current_col_index] = (pygame.draw.rect(screen, current_color,
                                                                        pygame.Rect(x_offset, y_offset, 128, 128)),
                                                       (x_offset, y_offset), (x_offset + 128, y_offset + 128))

        square_count += 1
        square_count_color_ref += 1
        current_col_index += 1
        x_offset += 128

        if square_count % 8 == 0:
            y_offset += 128
            x_offset = 0

            current_row_index += 1
            current_col_index = 0

            square_count_color_ref -= 1

def find_square_by_mouse_pos(mouse_pos):
    # find what square was clicked on
    for row in board:
        for square in row:
            top_left_corner = square[1]
            bottom_right_corner = square[2]

            top_x = top_left_corner[0]
            top_y = top_left_corner[1]

            bottom_x = bottom_right_corner[0]
            bottom_y = bottom_right_corner[1]

            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]

            if mouse_x >= top_x and mouse_x <= bottom_x:
                if mouse_y >= top_y and mouse_y <= bottom_y:
                    row_index = board.index(row)
                    col_index = row.index(square)

                    print(f"Found the square index: ({col_index}, {row_index})")


def draw_pieces():
    white_pawn = pygame.image.load("images/w_pawn_png_shadow_128px.png")
    white_rook = pygame.image.load("images/w_rook_png_shadow_128px.png")
    white_knight = pygame.image.load("images/w_knight_png_shadow_128px.png")
    white_bishop = pygame.image.load("images/w_bishop_png_shadow_128px.png")
    white_queen = pygame.image.load("images/w_queen_png_shadow_128px.png")
    white_king = pygame.image.load("images/w_king_png_shadow_128px.png")

    bottom_row_order = [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight,
                        white_rook]

    for square in board[6]:
        screen.blit(white_pawn, (square[1][0], square[1][1]))

    row_index = 0
    for square in board[7]:
        screen.blit(bottom_row_order[row_index], (square[1][0], square[1][1]))
        row_index += 1

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()

            # user left-clicked
            if mouse_presses[0]:
                mouse_pos = pygame.mouse.get_pos()
                find_square_by_mouse_pos(mouse_pos)




    draw_squares()
    draw_pieces()
    pygame.display.update()

pygame.quit()