#!/installer.py
# Written by Anthony Lucchese

import os
import shutil
import scanner
from sys import platform
import getpass


WINDOWS_OS = "nt"
MAC_OS = "posix"
WINDOWS_PATH_1 = "C:/Users/"
MAC_PATH_1 = "/Users/"
MINECRAFT_WINDOWS_PATH_2 = "/AppData/Roaming/.minecraft"
MINECTAFT_MAC_PATH_2 = "/Library/Application Support/minecraft"

popularGames = {
    "minecraftwin32": WINDOWS_PATH_1 + "USER" + MINECRAFT_WINDOWS_PATH_2, 
    "minecraftdarwin": MAC_PATH_1 + "USER" + MINECTAFT_MAC_PATH_2,

}

def init():
    initPath = os.getcwd() + "/games"
    if not os.path.isdir(initPath):
        print("Creating the /games/ directory...")
        os.mkdir("games")

def newGame() -> None:
    game = str(input("what is the name of the game:> ")).lower()
    mainGamesFolder = os.getcwd()
    gamePath = f"{mainGamesFolder}/games/{game}"
    if os.path.isdir(gamePath):
        print("This game already exists!")
        return
    addModsExtension = False
    gameModsFolder = ""
    if (game + platform) in popularGames:
        addModsExtension = True
        user = getpass.getuser()
        gameModsFolder = popularGames[game + platform].replace("USER", str(user))
    else:
        gameModsFolder = str(input("what is the folder location of the games mod folder? :>"))
    print("saving mods path...")
    os.mkdir(gamePath)
    scanner.createPathFile(gamePath, gameModsFolder, addModsExtension)
    if scanner.checkFolder(gameModsFolder):
        scanner.copyFiles(gameModsFolder, gamePath, addModsExtension)

    # add user IO
def removeGame(game: str) -> None:
    """Removes specified game from the available mods"""
    
    mainDir = os.getcwd()
    shutil.rmtree(f"{mainDir}/games/{game}", ignore_errors=True)
    os.chdir(mainDir)
    print(f"the local mods for {game} has been removed, but not the mods installed")
    