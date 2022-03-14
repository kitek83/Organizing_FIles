import shutil
from pathlib import Path

p = Path('C:/Users2/Kris')
#copy the file
shutil.copy(p/'sonnet29.txt',p/'spam')
#copy the folder
shutil.copytree(p/'newOsDirs', p/'newOsDirs_BackUp')