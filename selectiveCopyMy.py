#Program walks through the folder, subfolder, finds the files with giveb extension and copy them
#to another folder.

import os, shutil
from pathlib import Path


def copyFile(folder):
    absFolder = os.path.abspath(folder)
    print(absFolder)

    destination = Path('C:/Users2/7z')
    #walk through the folders and finding files with searhed extension
    #for folderName, subFolders, fileNames in os.walk(absFolder):
        #for fileName in fileNames:
           # if fileName.endswith('.7z'):
                #shutil.copy(absFolder/fileName, destination/fileName)
    for fileName in absFolder().glob('*.7z'):
        shutil.copy(absFolder/fileName, destination/fileName)





copyFile('C:/Users2/Kris')

#this one try not working