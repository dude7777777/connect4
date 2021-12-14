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

    def isThereAConnect4(self):
        #4 in a row
        #right
        #recursive(location, count, color, direction):
           # if(color == nextColor):
           #     count+=1
           #     recursive(nextLocation, count, color, direction)
        #up
        #up-right
        #up-left
        # catsgame
        return False
    
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