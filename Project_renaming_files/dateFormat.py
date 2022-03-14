import re,os
from pathlib import Path
import shutil

regexDate = re.compile(r"""(^.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)?\d\d)
(.*?)$
""",re.VERBOSE)
textDate = regexDate.search('The file sonnet10-20-1999kopia.txt is very important.')

print(textDate.group(8))
print('-------------------')
for file in os.listdir('.'):
    print(file)
print()
print(2*'-----------------')

p = Path('C:/Users2/Kris')
for file in os.listdir(p):
    print(file)
print()
print(2*'-----------------')

nameRegex = re.compile('Name:(.*) Last name:(.*)')
text = nameRegex.search('Name: Kris Last name: Kozak')
print(text.group(1))
print(text.group(2))