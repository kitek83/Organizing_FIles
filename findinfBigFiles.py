import os

direction = input('Enter folder path for searching big files: ')
direction = os.path.abspath(direction)

filesFound = ''
for folder, subFolders, fileNames in os.walk(direction):
    print('Searching the files in %s...' % folder)

    for fileName in fileNames:
        if os.path.getsize(os.path.join(folder,fileName)) >= 100000000:
            print('Found a file: %s' % fileName)
            filesFound += os.path.abspath(fileName)

print(filesFound)