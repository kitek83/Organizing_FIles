import zipfile
from pathlib import Path

p = Path('C:/Users2')
zipObject = zipfile.ZipFile(p/'Kris.zip')
zipObject.extractall('C:/Users2/KrisPythonExtract')
zipObject.close()