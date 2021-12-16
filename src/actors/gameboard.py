from src.utilities.matrix import Matrix
from src.utilities.enums.directions import Directions

class Gameboard:

    def __init__(self):
        self.blankSpot = ' '
        self.data = [ [' ' for j in range(7)] for i in range(6)]
        self.heights = [len(self.data)-1 for i in range (0,len(self.data[0]))]

    def printBoard(self):
        for i in range(0, len(self.data)):
            print(self.data[i])

    def isThereAConnect4(self, color):
        return (
            4 == self.check(Directions.UP, color) or
            4 == self.check(Directions.RIGHT, color) or
            4 == self.check(Directions.UP_RIGHT, color) or
            4 == self.check(Directions.DOWN_RIGHT, color)
        )

    def isThereATie(self):
        return self.blankSpot not in self.data[0]
    
    def check(self, direction, color):
        return Matrix.countCharsInDirection(direction=direction, matrix=self.data, target=color, maxCount=4)
    
    def validateDropLocation(self, dropLocation):
        try:
            column = int(dropLocation)
            assert(column >= 0)
            assert(column <= 6)
            row = self.heights[column]
            assert(row >= 0)
        except:
            return False
        return True

    def dropPiece(self, dropLocation, player):
        column = int(dropLocation)
        row = self.heights[column]
        self.data[row][column] = player.color
        self.heights[column]-=1