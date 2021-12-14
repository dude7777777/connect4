from actors.gameboard import Gameboard
from actors.player import Player

class Connect4:

    def __init__(self, player1):
        self.players = [player1, Player("Computer", "Black")]
        self.activePlayer = self.players[0]
        self.gameboard = Gameboard()
        self.turn = 0
        self.isGameOver = False

    def startGame(self):
        while not self.isGameOver:
            self.choosePlayer()
            self.updateDisplay()
            self.takeTurn()
            self.checkVictoryCondition()

    def updateDisplay(self):
        self.gameboard.printBoard()

    def choosePlayer(self):
        self.activePlayer = self.players[self.turn%2]
        print("Your turn, " + self.activePlayer.name)

    def takeTurn(self):
        dropLocation = input("Enter where you want to drop it [0-6]: ")
        while not (self.gameboard.validateDropLocation(dropLocation)):
            dropLocation = input("Enter where you want to drop it [0-6]: ")
        self.gameboard.dropPiece(dropLocation, self.activePlayer)
        self.turn+=1

    def checkVictoryCondition(self):
        if (self.gameboard.isThereAConnect4()):
            self.isGameOver = True