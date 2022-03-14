import os
from pathlib import Path

p = Path('C:/Users2/Kris')
print('-----------------')
print(os.path.abspath('.')) #current working folder
print('---------------------')
print(os.path.abspath(p))
for folderName in os.walk(p):
    print('FOLDER: ', folderName)
    for fileName in folderName:
        print('FILE DIR: ', folderName, ' : ', fileName)
