import FilePath
from FilePath import getFilePath, getFilePathByFolder
from FileOperation import doConvert, makeFileName

def startProcess():
    count = 0
    for filePath in listFile:
        fileOut = makeFileName(filePath)
        doConvert(filePath, fileOut)
        print('-->  Convert file', filePath, 'to', fileOut, 'successfully!')
        count += 1
    print('\n\n  ==>  Converted successfully total [', count, '] file[s].')

print('\n\n-->  Take one of two option down below:')
print('+----------------------------------------oOo----------------------------------------+')
print('|  [1]. Choose one or many files you want to convert to .srt.                       |')
print('|  [2]. Choose one folder, then we will convert all the files .vtt in this folder.  |')
print('|  [0]. Cancel.                                                                     |')
print('+----------------------------------------oOo----------------------------------------+')
while(True):
    key = input('-->  Enter your answer (1 or 2): ')
    if key == '1' or key == '2' or key == '0': 
        break
    else:
        print('-->  Bad answer. Press [0] to terminate.')

if int(key) == 1:
    print('-->  Let\'s start with choosing file.')
    listFile = getFilePath()
    startProcess()
elif int(key) == 2:
    print('-->  Let\'s start with choosing folder.')
    listFile = getFilePathByFolder()
    startProcess()

print('\n\n  Author: GhostRyuki')
input('\n  Press Enter to exit.')