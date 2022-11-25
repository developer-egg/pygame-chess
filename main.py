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


def flip_board():
    pieces = []

    for row in board:
        for square in row:
            if square.piece is not None:
                pieces.append(square.piece)
                square.piece = None

    # flip each piece's position
    for piece in pieces:
        piece.board_location = (piece.board_location[0], 7 - piece.board_location[1])
        piece.actual_location = (piece.board_location[0] * 128, piece.board_location[1] * 128)

    for row in board:
        for square in row:
            for piece in pieces:
                if square.top_left == piece.actual_location:
                    square.piece = piece




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


def find_square_by_pos(pos):
    # find what square was clicked on
    for row in board:
        for square in row:
            top_left_corner = square.top_left
            bottom_right_corner = square.bottom_right

            top_x = top_left_corner[0]
            top_y = top_left_corner[1]

            bottom_x = bottom_right_corner[0]
            bottom_y = bottom_right_corner[1]

            pos_x = pos[0]
            pos_y = pos[1]

            if pos_x >= top_x and pos_x <= bottom_x:
                if pos_y >= top_y and pos_y <= bottom_y:
                    row_index = board.index(row)
                    col_index = row.index(square)

                    # print(f"Found the square index: ({col_index}, {row_index})")
                    return (col_index, row_index)


has_drawn_initial_pieces = False

def draw_pieces():
    global has_drawn_initial_pieces

    white_pawn = pygame.image.load("images/w_pawn_png_shadow_128px.png")
    white_rook = pygame.image.load("images/w_rook_png_shadow_128px.png")
    white_knight = pygame.image.load("images/w_knight_png_shadow_128px.png")
    white_bishop = pygame.image.load("images/w_bishop_png_shadow_128px.png")
    white_queen = pygame.image.load("images/w_queen_png_shadow_128px.png")
    white_king = pygame.image.load("images/w_king_png_shadow_128px.png")

    black_pawn = pygame.image.load("images/b_pawn_png_shadow_128px.png")
    black_rook = pygame.image.load("images/b_rook_png_shadow_128px.png")
    black_knight = pygame.image.load("images/b_knight_png_shadow_128px.png")
    black_bishop = pygame.image.load("images/b_bishop_png_shadow_128px.png")
    black_queen = pygame.image.load("images/b_queen_png_shadow_128px.png")
    black_king = pygame.image.load("images/b_king_png_shadow_128px.png")

    row_order_strings = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]

    white_row_order = [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight,
                        white_rook]

    black_row_order = [black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight,
                       black_rook]

    if not has_drawn_initial_pieces:
        for board_square in board[6]:
            # add one so that the point is not on the edge
            top_x = board_square.top_left[0] + 1
            top_y = board_square.top_left[1] + 1

            board_location = find_square_by_pos((top_x, top_y))

            board_square.piece = piece.Piece("pawn", white_pawn, (top_x, top_y), (board_location), [], "white")
            screen.blit(white_pawn, (board_square.piece.actual_location[0], board_square.piece.actual_location[1]))

        row_order_index = 0

        for board_square in board[7]:
            # add one so that the point is not on the edge
            top_x = board_square.top_left[0] + 1
            top_y = board_square.top_left[1] + 1

            board_location = find_square_by_pos((top_x, top_y))

            board_square.piece = piece.Piece(row_order_strings[row_order_index], white_row_order[row_order_index], (top_x, top_y), (board_location), [], "white")
            row_order_index += 1


        for board_square in board[1]:
            # add one so that the point is not on the edge
            top_x = board_square.top_left[0] + 1
            top_y = board_square.top_left[1] + 1

            board_location = find_square_by_pos((top_x, top_y))

            board_square.piece = piece.Piece("pawn", black_pawn, (top_x, top_y), (board_location), [], "black")
            screen.blit(white_pawn, (board_square.piece.actual_location[0], board_square.piece.actual_location[1]))

        row_order_index = 0

        for board_square in board[0]:
            # add one so that the point is not on the edge
            top_x = board_square.top_left[0] + 1
            top_y = board_square.top_left[1] + 1

            board_location = find_square_by_pos((top_x, top_y))

            board_square.piece = piece.Piece(row_order_strings[row_order_index], black_row_order[row_order_index], (top_x, top_y), (board_location), [], "black")
            row_order_index += 1

        has_drawn_initial_pieces = True

    # draw pieces
    for board_row in board:
        for board_square in board_row:
            if board_square.piece is not None:
                # update legal moves
                board_square.piece.set_legal_moves(board)

                screen.blit(board_square.piece.image, (board_square.piece.actual_location[0], board_square.piece.actual_location[1]))

    # row_index = 0
    # for square in board[7]:
    #     piece = screen.blit(bottom_row_order[row_index], (square[1][0], square[1][1]))
    #     square.piece = piece
    #     row_index += 1


running = True

first_square = None
second_square = None

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
                square_pos = find_square_by_pos(mouse_pos)

                square = board[square_pos[1]][square_pos[0]]

                if square is not None:
                    if first_square is None and square.piece is not None:
                        first_square = square
                    elif first_square is not None:
                        second_square = square

                        legal_moves = first_square.piece.legal_moves
                        is_legal_move = False

                        for move in legal_moves:
                            if move == square_pos:
                                is_legal_move = True

                        # makes sure you cannot capture your own piece
                        if square.piece is not None:
                            if square.piece.team == first_square.piece.team:
                                is_legal_move = False

                        if is_legal_move:
                            # set the piece of the second
                            piece = first_square.piece
                            piece.actual_location = square.top_left
                            piece.board_location = square_pos

                            piece.set_legal_moves(board)

                            # check if there was a capture
                            if second_square.piece is not None and second_square.piece.team != first_square.piece.team:
                                print("capture!")


                            second_square.piece = first_square.piece

                            # set first_square piece to none
                            first_square.piece = None

                            # flip the board so the other player can make their move
                            flip_board()

                        first_square = None

    pygame.display.update()

pygame.quit()
