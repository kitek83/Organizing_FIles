import os
from pathlib import Path

p = Path('C:/Users2/Kris')
for folderName, subFolders, fieleNames in os.walk(p):
    print('Current folder is:' + folderName)
    for subFolder in subFolders:
        print('Subfolder of ' + folderName + ':' + subFolder)
        for fileName in fieleNames:
            print('FILE INSIDE ' + folderName + ':' + fileName)