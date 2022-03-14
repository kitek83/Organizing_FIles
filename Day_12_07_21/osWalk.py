import os
from pathlib import Path

p = Path('C:/Users2/Kris')
for folderName, subfolders, fileNames in os.walk(p):
    print('The current folder is: '+ folderName)
    for subfolder in subfolders:
        print('Subfolder of '+folderName+' : '+subfolder)
        for file in fileNames:
            print('File inside ' + folderName + ':' + file)






