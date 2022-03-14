import os, shutil

folder = input('Enter the folder from which you will copy the files: ')
extension = input('Enter extension of files to copy: ')
destination = input('Enter destination folder for copied files: ')

for folder, subFolders, fileNames in os.walk(folder):
    for fileName in fileNames:
        if fileName.endswith('{}'.format(extension)):
            shutil.copy(os.path.join(folder,fileName),destination)

print(f'Program copied files of extension:{extension} from '
      f'{os.path.basename(folder)} to {os.path.basename(destination)}.')