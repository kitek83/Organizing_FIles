import os, re, shutil

americanDate = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$""", re.VERBOSE)

for americanFile in os.listdir('.'):

    dateFind = americanDate.search(americanFile)
    if dateFind == None:
        continue
    #construction of americac file, which will be changed on Eurofile
    beforeDate = dateFind.group(1)
    month = dateFind.group(2)
    day = dateFind.group(4)
    year = dateFind.group(6)
    afterDate = dateFind.group(8)

    #Form the european style filename.
    euroFile = beforeDate + day + '-' + month + '-' + year + afterDate

    #Get the full absolute file patch.
    workingDir = os.path.abspath('.')
    amerFile = os.path.join(workingDir, americanFile)
    eurFile = os.path.join(workingDir, euroFile)

    print(f'Renaming the file {amerFile} to {eurFile}.')
    shutil.move(amerFile, eurFile)