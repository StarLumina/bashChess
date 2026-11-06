from board import ChessBoard
from pieces import *

def main():
    #newBoard = ChessBoard()
    #newBoard.print_board()
    pawn = Pawn("White", "e2")
    pawn.getPossibleMoves()

main()