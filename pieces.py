from constants import FILETRANSLATOR, FILETRANSLATOREVERSE

class Piece:
    def __init__(self, color, coords):
        self.color = color
        self.coords = coords
        self.possibleMoves = []
    
    def move(self, newCoords):
        if newCoords in self.possibleMoves:
            self.coords = newCoords
            self.possibleMoves = self.getPossibleMoves()
            return True
        else:
            print("not a legal move")
            return False

    def getFile(self) -> int:
        return self.coords[0]
        
    def getRank(self) -> int:
        return int(self.coords[1])
        
    def getPossibleMoves(self):
        pass
        


class Pawn(Piece):
    def __init__(self, color, coords):
        super().__init__(color, coords)
        if self.color == "Black":
            self.possibleMoves = [f"{self.getFile()}{self.getRank() - 1}", f"{self.getFile()}{self.getRank() - 2}"]
        else:
            self.possibleMoves = [f"{self.getFile()}{self.getRank() + 1}", f"{self.getFile()}{self.getRank() + 2}"]

    def move(self, newCoords):
        if newCoords in self.possibleMoves:
            self.coords = newCoords
            self.getPossibleMoves(self.coords)
            return True
        else:
            print("not a legal move")
            return False

    def getPossibleMoves(self):
        print(self.possibleMoves)


