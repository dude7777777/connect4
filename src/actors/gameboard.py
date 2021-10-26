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

    def isGameOn(self):
        return True