#program copies files with given extension from given folder to given destination
import os
import shutil

folder = input('Enter the folder, from which you want to copy the files with given extension: ')
extension = input('Enter the extension of files, you want to copy:')
destination = input('Enter destination folder for copied files: ')

for folder, subFolders, files in os.walk(folder):
    for file in files:
        if file.endswith('{}'.format(extension)):  #formating extension to string --> 'extension'
            shutil.copy(os.path.join(folder,file),destination)

print(f'Program copied files with extension {extension} from the'
      f'folder {os.path.basename(folder)} to {os.path.basename(destination)}')