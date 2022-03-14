import os, shutil
from pathlib import Path

p = Path('C:/Users2/Kris')
print(p.exists())
shutil.copy(p/'details.csv', p/'spam')
shutil.copy(p/'hello.txt',p/'spam/helox.txt')