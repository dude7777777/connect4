from src.actors.player import Player
from src.actors.connect4 import Connect4

def main():
    print("Welcome to Connect4")
    connect4 = Connect4(Player("Jacob", "Red"))
    connect4.startGame()

if __name__ == "__main__":
    main()