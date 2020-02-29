import re

def makeFileName(fileBase):
    newFName = re.sub(r'.vtt$', '', fileBase) 
    return  newFName + '.srt'
def convertTime(string):
    confirm = re.search(' --> ', string)
    if confirm:
        strIn = string.split(' --> ')
        match = re.sub(r'[.]{1}', ',', strIn[0])
        sout = '00:' + match
        strOut = sout
        match = re.sub(r'[.]{1}', ',', strIn[1])
        sout = '00:' + match
        strOut += ' --> ' + sout
        return strOut
    else:
        return ''

def doConvert(fileIn, fileOut):
    fin = open(fileIn, "r", errors='ignore')
    fout = open(fileOut, "w")
    numberSub = 0
    inc = 0
    listline = []
    for line in fin:
        if numberSub == 0:
            numberSub = 1
            continue
        listline.append(line)
        inc += 1
        if inc == 3:
            fout.write(str(numberSub) + '\n')
            fout.write(convertTime(listline[1]))
            fout.write(listline[2] + '\n')
            inc = 0
            numberSub += 1
            listline.clear()
    fin.close()
    fout.close()