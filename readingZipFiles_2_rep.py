import zipfile
from pathlib import Path
p = Path('C:/Users2')
zipFileObject = zipfile.ZipFile(p/'Kris.zip')
print(zipFileObject.namelist())
sonnet29GetInfo = zipFileObject.getinfo('Kris/sonnet29.txt')
print('file size is:',sonnet29GetInfo.file_size)
print('compressed files size is:',sonnet29GetInfo.compress_size)
print(f'Compressed files is {round(sonnet29GetInfo.file_size/sonnet29GetInfo.compress_size,2)}x smaller.')
zipFileObject.close()
