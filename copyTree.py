import shutil, os
from pathlib import Path

p = Path('C:/Users2')
#shutil.copytree(p/'Kris',p/'Kris_backup')

p2 = Path('C:/Users2/Kris')
#print(shutil.copytree(p2/'spam',p2/'spam_back_up'))

shutil.move('C:\\Users2\\Kris\\details3.csv','C:\\Users2\\Kris\\spam')