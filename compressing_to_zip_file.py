import zipfile
from pathlib import Path

p1 = Path('C:/Users2/Kris')
p2 = Path('C:/Users2/Kris_backup')

zipObject = zipfile.ZipFile(p2/'python2Compressed.zip','w')
zipObject.write(p1/'details2.csv',compress_type=zipfile.ZIP_DEFLATED)
zipObject.close()


