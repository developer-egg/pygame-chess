class Piece:
    def __init__(self, type, image, actual_location, board_location, legal_moves, team):
        self.type = type
        self.actual_location = actual_location
        self.board_location = board_location
        self.legal_moves = legal_moves
