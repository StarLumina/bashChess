class Piece:
    def __init__(self, color, rank, file):
        self.color = color
        self.rank = rank
        self.file = file

    def move():
        pass

class Pawn(Piece):
    def __init__(self, color, rank, file):
        super().__init__(self, color, rank, file)
        self.hasMoved = False
        pass

    def move():
        pass

