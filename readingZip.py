import zipfile
import os
from pathlib import Path

p = Path('C:\\Users2')
#open zipfile
zipExample = zipfile.ZipFile(p/'Kris.zip')
print(zipExample.namelist())
fileInfo = zipExample.getinfo('Kris/sonnet29.txt')
print('file size: ',fileInfo.file_size)
print('compressed file size:',fileInfo.compress_size)
print(f'Compressed file is {round(fileInfo.file_size/fileInfo.compress_size,2)} x smaller.')
