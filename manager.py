
import os
import shutil

def listGames():
    mainPath = os.getcwd()
    if mainPath.split("/")[-1] != "games":
        mainPath += "/games"
    files = os.listdir(mainPath)
    files.remove(".DS_Store")
    print(", ".join(files))

def pushMods(game: str):
    fromFolder = f"{os.getcwd()}/games/{game}"
    if not os.path.isdir(fromFolder):
        return
    print("adding mods to mods folder...")
    toFolder = ""
    with open((fromFolder + "/.path"), "r") as f:
        toFolder = f.read()
    for file in os.listdir(fromFolder):
        if file not in [".path", ".DS_Store"]:
            shutil.move(f"{fromFolder}/{file}", toFolder)    

def pullMods(game: str):
    toFolder = f"{os.getcwd()}/games/{game}"
    if not os.path.isdir(toFolder):
        return
    print("adding mods to mods folder...")
    fromFolder = ""
    with open((toFolder + "/.path"), "r") as f:
        fromFolder = f.read()
    for file in os.listdir(fromFolder):
        if file not in [".path", ".DS_Store"]:
            shutil.move(f"{fromFolder}/{file}", toFolder)