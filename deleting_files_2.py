from pathlib import Path
import os

for fileName in Path('C:/Users2/Kris').glob('*.rtxt'):
    os.unlink(fileName)