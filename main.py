import installer
import scanner
import os



def main():
    installer.init()
    prompt = str(input("What would you like to do (0: exit, 1: add new game, 2: remove a game, 3: list games):> "))
    while(prompt != "0"):
        if (prompt == "1"):
            installer.newGame() 
        elif (prompt == "2"):
            installer.removeGame()
        elif (prompt == "3"):
            installer.listGames()
        prompt = str(input("What would you like to do (0: exit, 1: add new game, 2: remove a game, 3: list games):> "))
if __name__ == "__main__":
    main()
