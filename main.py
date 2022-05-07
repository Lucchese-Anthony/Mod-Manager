#!/main.py
# Written by Anthony Lucchese

import installer
import scanner
import manager
import os

def main():
    installer.init()
    prompt = str(input("What would you like to do (h: help):> "))
    while(prompt != "0"):
        if (prompt == "1"):
            installer.newGame() 
        elif (prompt == "2"):
            game = str(input("what is the name of the game:> ")).lower()
            installer.removeGame(game)
        elif (prompt == "3"):
            manager.listGames()
        elif (prompt == "4"):
            game = str(input("what is the name of the game:> ")).lower()
            manager.pushMods(game)
        elif (prompt == "5"):
            game = str(input("what is the name of the game:> ")).lower()
            manager.pullMods(game)
        elif (prompt == "h"):
            print("0: exit, 1: add new game, 2: remove a game, 3: list games")
        else:
            print("incorrect input...")
        prompt = str(input("What would you like to do (h: help):> "))
if __name__ == "__main__":
    main()
