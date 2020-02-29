def makeFileName(fileBase):
    newFName = fileBase.replace('.vtt', '.srt')
    return  newFName

def convertTime(string):
    if string.find(' --> ') != -1:
        strIn = string.replace('.', ',')
        strOut = '00:'+ strIn[0:14] + '00:'+ strIn[14:] 
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