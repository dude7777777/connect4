from actors.gameboard import Gameboard
from actors.player import Player

def main():
    print("Welcome to Connect4", end=" ")

    jacob = Player("Jacob")
    jacob.printName()

    gameboard = Gameboard()
    gameboard.printBoard()

if __name__ == "__main__":
    main()