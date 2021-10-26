from gameboard import Gameboard
from player import Player

class Connect4:

    def __init__(self):
        self.players = [Player("Jacob"), Player("Computer")]
        self.activePlayer = self.players[1]
        self.gameboard = Gameboard()
        self.turn = 0
        self.isGameOver = False

        self.startGame()

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

    def takeTurn(self):
        # choose drop location from keyboard
        # check if valid spot
        # subtract token from collection
        self.turn=+1

    def checkVictoryCondition(self):
        self.isGameOver = True