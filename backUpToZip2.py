#!python 3
#backUpToZip2.py - Copiers an entire folder and its conbtencts into
# a ZIP file whose file name increments.

import os, zipfile

def backUpToZip(folder):
    currentFolder = os.path.abspath(folder)
    print(currentFolder)

    number = 1
    #creating the name of zip file
    while True:
        zipeFileName = os.path.basename(currentFolder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipeFileName):
            break
        number += 1
    #Creat the zipfile.
    backUpZipFile = zipfile.ZipFile(zipeFileName,'w')
    #Walk the entire folder tree and compress the files in each folder.
    for folderName, subfolders, fileNames in os.walk(currentFolder):
        #Adding folder name
        backUpZipFile.write(folderName)
        #Add all files in this folder to the zip file.
        for file in fileNames:
            newBase = os.path.basename(currentFolder) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue
            backUpZipFile.write(os.path.join(folderName,file))
    backUpZipFile.close()



backUpToZip('C:/Users2/Kris')