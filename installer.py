import os
import shutil
import scanner
from sys import platform

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

def newGame():
    game = str(input("what is the name of the game:> ")).lower()
    mainGamesFolder = os.getcwd()
    gamePath = f"{mainGamesFolder}/games/{game}"
    if os.path.isdir(gamePath):
        print("This game already exists!")
        return
    os.mkdir(gamePath)
    
    gameModsFolder = ""
    if (game + platform) in popularGames:
        user = os.environ.get("USERNAME")
        gameModsFolder = popularGames[game + platform].replace("USER", user)
    else:
        gameModsFolder = str(input("what is the folder location of the games mod folder? :>"))
    print("saving mods path...")
    scanner.createPathFile(gamePath, gameModsFolder)
    if scanner.checkFolder(gameModsFolder):
        scanner.copyFiles(gameModsFolder, gamePath)

    # add user IO
def removeGame():
    mainDir = os.getcwd()
    game = str(input("what is the name of the game:> "))
    shutil.rmtree(f"{mainDir}/games/{game}", ignore_errors=True)
    os.chdir(mainDir)
    print(f"the local mods for {game} has been removed, but not the mods installed")
    

def listGames():
    mainPath = os.getcwd()
    if mainPath.split("/")[-1] != "games":
        os.chdir(mainPath + "/games")
    files = os.listdir(mainPath)
    files.remove(".DS_Store")
    print(", ".join(files))
