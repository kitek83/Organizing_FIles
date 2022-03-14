import zipfile,os

def backUpToZip(folder):
    folder = os.path.abspath(folder)
    print(folder)

    #checking if exists another zip files with the same name
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1
    #create the zip file
    backUpZip = zipfile.ZipFile(zipFileName,'w')
    #walk entire folder tree and compress the files in each folder
    for folder, subFolders, fileNames in os.walk(folder):
        print(f'Adding {folder} to zip file...')
        backUpZip.write(folder)
        for fileName in fileNames:
            newBase = os.path.basename(folder) + '_'
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                continue
            backUpZip.write(os.path.join(folder,fileName))
    backUpZip.close()

backUpToZip('C:/Users2/Kris')