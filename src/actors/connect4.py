from src.actors.gameboard import Gameboard
from src.actors.player import Player

class Connect4:

    def __init__(self, player1):
        self.players = [player1, Player("Computer", "O")]
        self.activePlayer = self.players[0]
        self.gameboard = Gameboard()
        self.turn = 0
        self.isGameOver = False

    def startGame(self):
        while not self.isGameOver:
            self.choosePlayer()
            self.updateDisplay()
            self.takeTurn()
            self.updateDisplay()
            self.checkVictoryCondition()

    def updateDisplay(self):
        self.gameboard.printBoard()

    def choosePlayer(self):
        self.activePlayer = self.players[self.turn%2]
        print("\nYour turn, " + self.activePlayer.name + ": " + self.activePlayer.color)

    def takeTurn(self):
        dropLocation = input("Enter where you want to drop it [0-6]: ")
        while not (self.gameboard.validateDropLocation(dropLocation)):
            dropLocation = input("Enter where you want to drop it [0-6]: ")
        self.gameboard.dropPiece(dropLocation, self.activePlayer)
        self.turn+=1

    def checkVictoryCondition(self):
        if (self.gameboard.isThereAConnect4(self.activePlayer.color)):
            self.isGameOver = True
            print("Connect4!!! Winner: " + self.activePlayer.name)
        elif (self.gameboard.isThereATie()):
            self.isGameOver = True
            print("Wow, it's a tie!")