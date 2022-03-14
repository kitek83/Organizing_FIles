import zipfile
from pathlib import Path

p = Path('C:\\Python projects\\Python Projects\\python repetition1\\Automate_book\\Chapter10_Organizing_Files')
zipExtract = zipfile.ZipFile(p/'Kris_1.zip')
zipExtract.extractall()
zipExtract.close()