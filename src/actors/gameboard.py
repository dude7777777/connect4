from src.utilities.matrix import Matrix
from src.utilities.enums.directions import Directions

class Gameboard:

    def __init__(self):
        self.data = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]

        self.heights = [len(self.data)-1 for i in range (0,len(self.data[0]))]

    def printBoard(self):
        for i in range(0, len(self.data)):
            print(self.data[i])

    def isThereAConnect4(self, color):
        return (
            0 not in self.data[0] or
            4 == Matrix.countCharsInDirection(direction=Directions.UP, matrix=self.data, target=color, maxCount=4) or
            4 == Matrix.countCharsInDirection(direction=Directions.RIGHT, matrix=self.data, target=color, maxCount=4) or
            4 == Matrix.countCharsInDirection(direction=Directions.UP_RIGHT, matrix=self.data, target=color, maxCount=4) or
            4 == Matrix.countCharsInDirection(direction=Directions.DOWN_RIGHT, matrix=self.data, target=color, maxCount=4)
        )
    
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