#program copies files with given extension from given folder to given destination
import os,shutil

folder = input('Enter anblouth path of the folder, from which one you want to copy files: ')
extension = input('Enter the extension of the files, you want to copy: ')
destination = input('Enter destination folde for copied files: ')

for folder, subFolders, fileNames in os.walk(folder):
    for fileName in fileNames:
        if fileName.endswith('{}'.format(extension)):
            shutil.copy(os.path.join(folder,fileName),destination)
print('Selective copying has finished - all files of', extension,
      'type have been copied from',os.path.basename(folder), 'to',
      os.path.basename(destination))

