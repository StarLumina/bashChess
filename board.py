from constants import *

class ChessBoard:
    def  __init__(self):
        self.board = [
            [Square("white", 8, 1), Square("black", 8, 2), Square("white", 8, 3), Square("black", 8, 4), Square("white", 8, 5), Square("black", 8, 6), Square("white", 8, 7), Square("black", 8, 8)],
            [Square("black", 7, 1), Square("white", 7, 2), Square("black", 7, 3), Square("white", 7, 4), Square("black", 7, 5), Square("white", 7, 6), Square("black", 7, 7), Square("white", 7, 8)],
            [Square("white", 6, 1), Square("black", 6, 2), Square("white", 6, 3), Square("black", 6, 4), Square("white", 6, 5), Square("black", 6, 6), Square("white", 6, 7), Square("black", 6, 8)],
            [Square("black", 5, 1), Square("white", 5, 2), Square("black", 5, 3), Square("white", 5, 4), Square("black", 5, 5), Square("white", 5, 6), Square("black", 5, 7), Square("white", 5, 8)],
            [Square("white", 4, 1), Square("black", 4, 2), Square("white", 4, 3), Square("black", 4, 4), Square("white", 4, 5), Square("black", 4, 6), Square("white", 4, 7), Square("black", 4, 8)],
            [Square("black", 3, 1), Square("white", 3, 2), Square("black", 3, 3), Square("white", 3, 4), Square("black", 3, 5), Square("white", 3, 6), Square("black", 3, 7), Square("white", 3, 8)],
            [Square("white", 2, 1), Square("black", 2, 2), Square("white", 2, 3), Square("black", 2, 4), Square("white", 2, 5), Square("black", 2, 6), Square("white", 2, 7), Square("black", 2, 8)],
            [Square("black", 1, 1), Square("white", 1, 2), Square("black", 1, 3), Square("white", 1, 4), Square("black", 1, 5), Square("white", 1, 6), Square("black", 1, 7), Square("white", 1, 8)]
        ]

    def print_board(self):
        string_board = ""
        for rank in self.board:
            rank_to_print = "| "
            for square in rank:
                rank_to_print += f"{square.color} : {FILETRANSLATOR[square.file]}{square.rank} | "
            rank_to_print += "\n"
            string_board += rank_to_print

        print(string_board)

    def initialize_game():
        pass

    def turn():
        pass

    def win():
        pass



class Square:
    def __init__(self, color, rank, file):
        self.color = color
        self.rank = rank
        self.file = file