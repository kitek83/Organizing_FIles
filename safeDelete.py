import send2trash

newFile = open('Bacon.txt','a')
newFile.write('Bacom is not a vegetable.')
newFile.close()

send2trash.send2trash('Bacon.txt')