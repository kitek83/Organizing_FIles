#python3
#renameDates.py - Rename files containing dates with American mm-dd-yyyy day format
#to Erupean dd-mm-yyyy format.
import re,os,shutil
#1.Creatind date pttern to find files with American date format
datePattern = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)?\d\d)
(.*?)$
""",re.VERBOSE)

#2.Loop over the files in the working directory.
#'.' - means working directory
for americanFile in os.listdir('.'):
    #skip files iwthour the date
    findFile = datePattern.search(americanFile)
    #skipe the file if there is no date and start looping from the beginning
    if findFile == None:
        continue
    #3.Get different part of the filename

    beforeDate = findFile.group(1)
    month = findFile.group(2)
    day = findFile.group(4)
    year = findFile.group(6)
    afterYear = findFile.group(8)

    #4.Form the European-style filename.
    euroFile = beforeDate + day + '-' + month + '-' + year + afterYear
    print('eurofile is: ',euroFile)
    #5.Get the full, absolute file path
    workingDir = os.path.abspath('.')
    print('Working directory:',workingDir)

    americanFile = os.path.join(workingDir,americanFile)
    print('american file path:',americanFile)

    euroFile = os.path.join(workingDir, euroFile)
    print('euroFile path:',euroFile)

    #6.Rename the files using shutil.moove
    print()
    print(f'Renaming {americanFile} to {euroFile}.')
    shutil.move(americanFile,euroFile)




























