#!/scanner.py
# Written by Anthony Lucchese

import os
import shutil
from distutils.dir_util import copy_tree

def copyFiles(fromFolder:str, toFolder:str, addModsExtension:bool):
    print(f"copying the files from {fromFolder} into {toFolder}")
    if fromFolder.split("/")[-1] != "mods" and addModsExtension:
        fromFolder += "/mods"
    print("the files include:")
    print("\n".join(os.listdir(fromFolder)))
    copy_tree(fromFolder, toFolder)    

def checkFolder(folder:str):
    print(f"{folder} | {os.path.isdir(folder)}")
    return os.path.isdir(folder)

def createPathFile(folder:str, location:str, addModsExtension:bool):
    with open((folder + "/.path"), "w+") as f:
        if addModsExtension:
            location += "/mods"
        f.write(location)

