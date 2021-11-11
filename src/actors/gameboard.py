class Gameboard:

    def __init__(self):
        self.data = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]

    def printBoard(self):
        for i in range(0, len(self.data)):
            print(self.data[i])

    def isThereAConnect4(self):
        # TODO add logic
        return True
    
    def validateDropLocation(self, dropLocation):
        # TODO add logic
        return True

    def dropPiece(self, dropLocation, player):
        # TODO add logic
        self.data[5][int(dropLocation)] = player.color