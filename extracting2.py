import zipfile
from pathlib import Path

p = Path('C:/Users2/Kris_backup')
zipObject = zipfile.ZipFile(p/'python2Compressed.zip')
zipObject.extractall(p)
