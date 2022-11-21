class Square:
    is_occupied = False

    def __init__(self, square, top_left, bottom_right, piece):
        self.square = square
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.piece = piece
