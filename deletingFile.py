import os, shutil
from pathlib import Path

for file in Path('C:\\Users2\\Kris\\spam').glob('*rxt'):
    os.unlink(file)