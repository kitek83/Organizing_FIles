import zipfile,os
def backUpToZipFile(folder):
    #make  sure folder is absolute
    folderExist = os.path.abspath(folder)
    #Figure out the filename this code should be used based on what files already exists.
    number = 1
    while True:
        nameFileZip = os.path.basename(folderExist) + '_' + str(number) + '.zip'
        if not os.path.exists(nameFileZip):
            break
        number += 1
    #Create the zipfile
    print(f'Creating zipfile {nameFileZip}...')
    newZipFile = zipfile.ZipFile(nameFileZip,'w')

    #Walk the entire folder tree and compress the files in each folder
    for folderName, subfolders, filenames in os.walk(folder):
        #adding foldeName to zip
        newZipFile.write(folderName)
        for fileName in filenames:
            newBase = os.path.basename(folder) + '_'
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                continue
            newZipFile.write(os.path.join(folderName,fileName))
    newZipFile.close()

backUpToZipFile('C:/Users2/Kris')