import pygame
import square
import piece

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

        rect = pygame.draw.rect(screen, current_color, pygame.Rect(x_offset, y_offset, 128, 128))

        if board[current_row_index][current_col_index] is None:
            board[current_row_index][current_col_index] = square.Square(rect, (x_offset, y_offset),
                                                                        (x_offset + 128, y_offset + 128), None)

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


def find_square_by_pos(mouse_pos):
    # find what square was clicked on
    for row in board:
        for square in row:
            top_left_corner = square.top_left
            bottom_right_corner = square.bottom_right

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

                    # print(f"Found the square index: ({col_index}, {row_index})")
                    return (col_index, row_index)


def draw_pieces():
    white_pawn = pygame.image.load("images/w_pawn_png_shadow_128px.png")
    white_rook = pygame.image.load("images/w_rook_png_shadow_128px.png")
    white_knight = pygame.image.load("images/w_knight_png_shadow_128px.png")
    white_bishop = pygame.image.load("images/w_bishop_png_shadow_128px.png")
    white_queen = pygame.image.load("images/w_queen_png_shadow_128px.png")
    white_king = pygame.image.load("images/w_king_png_shadow_128px.png")

    bottom_row_order = [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight,
                        white_rook]

    for board_square in board[6]:
        top_x = board_square.top_left[0]
        top_y = board_square.top_left[1]

        find_square_by_pos((top_x, top_y))

        board_location = find_square_by_pos((top_x, top_y))

        board_square.piece = piece.Piece("pawn", white_pawn, (top_x, top_y), (board_location))
        screen.blit(white_pawn, (board_square.piece.actual_location[0], board_square.piece.actual_location[1]))

    # row_index = 0
    # for square in board[7]:
    #     piece = screen.blit(bottom_row_order[row_index], (square[1][0], square[1][1]))
    #     square.piece = piece
    #     row_index += 1


running = True

while running:
    draw_squares()
    draw_pieces()

    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()

            # user left-clicked
            if mouse_presses[0]:
                mouse_pos = pygame.mouse.get_pos()
                find_square_by_pos(mouse_pos)

    pygame.display.update()

pygame.quit()
