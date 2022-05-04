import os
import shutil

WINDOWS_OS = "nt"
MAC_OS = "posix"
WINDOWS_PATH_1 = "C:/Users/"
MAC_PATH_1 = "/Users/"
MINECRAFT_WINDOWS_PATH_2 = "/AppData/Roaming/.minecraft/mods"
MINECTAFT_MAC_PATH_2 = "/Library/Application Support/minecraft"

def init():
    initPath = os.getcwd() + "/games"
    if not os.path.isdir(initPath):
        print("Creating the /games/ directory...")
        os.mkdir("games")

def newGame():
    game = str(input("what is the name of the game:> "))
    mainPath = os.getcwd() + "/games"
    os.chdir(mainPath)
    gamePath = f"{mainPath}/{game}"
    if os.path.isdir(gamePath):
        print("This game already exists!")
        return
    os.mkdir(gamePath)
    os.chdir(gamePath)
    modsPath = str(input("what is the path of the mods folder:> "))
    localModsPath = f"{gamePath}/.path"
    with open(".path", "w+") as f:
        f.write(modsPath)
    files = os.listdir(modsPath)
    print(f"copying the files from {modsPath} into {localModsPath}")
    print("the files include:")
    print("\n".join(files))
    for file_name in files:
        shutil.copy2(os.path.join(modsPath, file_name), localModsPath)    
    os.chdir(mainPath)

    # add user IO
def removeGame():
    mainDir = os.getcwd()
    game = str(input("what is the name of the game:> "))
    shutil.rmtree(f"{mainDir}/games/{game}", ignore_errors=True)
    os.chdir(mainDir)
    print(f"the mods for {game} has been removed...")
    

def listGames():
    mainPath = os.getcwd()
    if mainPath.split("/")[-1] != "games":
        os.chdir(mainPath + "/games")
    files = os.listdir()
    files.remove(".DS_Store")
    print(", ".join(files))
