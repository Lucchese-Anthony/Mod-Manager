import os
import shutil

def main():
    print("hello!")

def copyFiles(fromFolder:str, toFolder:str):
    print(f"copying the files from {fromFolder} into {toFolder}")
    if fromFolder.split("/")[-1] != "mods":
        fromFolder += "/mods"
    print("the files include:")
    files = os.listdir(fromFolder)
    print("\n".join(files))
    for file_name in files:
        shutil.copy(f"{fromFolder}/{file_name}", toFolder)    

def checkFolder(folder:str):
    return os.path.isdir(folder + "/mods")

def createPathFile(folder:str, location:str):
    with open((folder + "/.path"), "w+") as f:
        f.write(location + "/mods")

