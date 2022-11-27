class Piece:
    def __init__(self, type, image, actual_location, board_location, legal_moves, team):
        self.type = type
        self.image = image
        self.actual_location = actual_location
        self.board_location = board_location
        self.legal_moves = legal_moves
        self.team = team

    def set_legal_moves(self, board):
        # clear the list of legal moves first
        self.legal_moves = []

        board_location_x = self.board_location[0]
        board_location_y = self.board_location[1]

        if self.type == "pawn":
            square_ahead = None

            try:
                square_ahead = board[board_location_y - 1][board_location_x]
            except IndexError:
                pass

            if square_ahead is not None:
                if square_ahead.piece is None:
                    # can move forward if there is no enemy piece ahead
                    self.legal_moves.append((self.board_location[0], self.board_location[1] - 1))

            # can move two squares up if in starting position
            if self.board_location[1] == 6:
                self.legal_moves.append((self.board_location[0], self.board_location[1] - 2))

            right_diagonal_square = None
            left_diagonal_square = None

            try:
                right_diagonal_square = board[board_location_y - 1][board_location_x + 1]
            except IndexError:
                # right diagonal square is None
                pass

            if right_diagonal_square is not None and right_diagonal_square.piece is not None:
                self.legal_moves.append(right_diagonal_square.piece.board_location)

            try:
                left_diagonal_square = board[self.board_location[1] - 1][self.board_location[0] - 1]
            except IndexError:
                pass

            if left_diagonal_square is not None and left_diagonal_square.piece is not None:
                self.legal_moves.append(left_diagonal_square.piece.board_location)

        elif self.type == "knight":
            # for bishop and rook, make a loop and use multiplication or powers to generate this list
            positions_to_check = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

            for pos in positions_to_check:
                posX = pos[0]
                posY = pos[1]

                try:
                    # first test if the square exists
                    board[board_location_y + posY][board_location_x + posX]

                    # make sure board coords are not inverted for this one
                    self.legal_moves.append((board_location_x + posX, board_location_y + posY))
                except IndexError:
                    pass

        elif self.type == "king":
            positions_to_check = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

            for pos in positions_to_check:
                posX = pos[0]
                posY = pos[1]

                try:
                    # first test if the square exists
                    board[board_location_y + posY][board_location_x + posX]

                    # make sure board coords are not inverted for this one
                    self.legal_moves.append((board_location_x + posX, board_location_y + posY))
                except IndexError:
                    pass

        elif self.type == "bishop":
            up_and_right_positions = []
            up_and_left_positions = []
            down_and_right_positions = []
            down_and_left_positions = []

            # up and right diagonal
            for count in range(1, 8):
                up_and_right_positions.append((count, count))

            # up and left diagonal
            for count in range(1, 8):
                up_and_left_positions.append((-count, count))

            # down and right diagonal
            for count in range(1, 8):
                up_and_left_positions.append((count, -count))

            # down and left diagonal
            for count in range(1, 8):
                up_and_left_positions.append((-count, -count))

            for pos in up_and_right_positions:
                posX = pos[0]
                posY = pos[1]

                try:
                    # first test if the square exists
                    square = board[board_location_y + posY][board_location_x + posX]

                    # if there is a piece in that position, don't allow "jumping" over it
                    if square.piece is not None:
                        break
                except IndexError:
                    pass

            for pos in up_and_left_positions:
                posX = pos[0]
                posY = pos[1]

                try:
                    # first test if the square exists
                    square = board[board_location_y + posY][board_location_x + posX]

                    # if there is a piece in that position, don't allow "jumping" over it
                    if square.piece is not None:
                        break
                except IndexError:
                    pass

            for pos in down_and_right_positions:
                posX = pos[0]
                posY = pos[1]

                try:
                    # first test if the square exists
                    square = board[board_location_y + posY][board_location_x + posX]

                    # if there is a piece in that position, don't allow "jumping" over it
                    if square.piece is not None:
                        print('test')
                        break
                except IndexError:
                    pass

            for pos in down_and_left_positions:
                posX = pos[0]
                posY = pos[1]

                try:
                    # first test if the square exists
                    square = board[board_location_y + posY][board_location_x + posX]

                    # if there is a piece in that position, don't allow "jumping" over it
                    if square.piece is not None:
                        break
                except IndexError:
                    pass

            # add the legal moves
            positions = [up_and_right_positions, up_and_left_positions, down_and_left_positions, down_and_right_positions]

            for position_type in positions:
                for pos in position_type:
                    posX = pos[0]
                    posY = pos[1]

                    self.legal_moves.append((board_location_x + posX, board_location_y + posY))


        # elif self.type == "rook":
        #     up_and_right_positions = []
        #     up_and_left_positions = []
        #     down_and_right_positions = []
        #     down_and_left_positions = []
        #
        #     # up and right diagonal
        #     for count in range(1, 8):
        #         up_and_right_positions.append((count, count))
        #
        #     # up and left diagonal
        #     for count in range(1, 8):
        #         up_and_left_positions.append((-count, count))
        #
        #     # down and right diagonal
        #     for count in range(1, 8):
        #         up_and_left_positions.append((count, -count))
        #
        #     # down and left diagonal
        #     for count in range(1, 8):
        #         up_and_left_positions.append((-count, -count))




