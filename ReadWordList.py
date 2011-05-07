#!/usr/bin/env python

def __getRandIndex(itemsList):

    import random

    if len(itemsList) > 0:
        return random.randrange(len(itemsList))
    else:
        return -1

def pickWordAtRandom(pathToFileOrDir=None):

    import sys, os, os.path

    if not os.path.exists(pathToFileOrDir):
        print "Path '%s' does not exist!" % pathToFileOrDir
        sys.exit(1)

    elif os.path.isdir(pathToFileOrDir):
        filesList = os.listdir(pathToFileOrDir)
        randomIndex = __getRandIndex(filesList)

        if randomIndex == -1:
            return "Directory '%s' is empty!" % os.path.split(pathToFileOrDir)[1]

        filePath = os.path.join(pathToFileOrDir, filesList[randomIndex])

    elif os.path.isfile(pathToFileOrDir):
        filePath = pathToFileOrDir

    filePointer = open(filePath, 'rb')
    linesList = filePointer.readlines()
    filePointer.close()

    randomIndex = __getRandIndex(linesList)

    if randomIndex == -1:
        return "File '%s' is empty!" % os.path.split(filePath)[1]

    randomLine = linesList[randomIndex]
    randomWord = randomLine.replace('\n','')

    indexOfParanthesis = randomWord.find('(')

    if indexOfParanthesis>0:
        randomWord = randomWord[:indexOfParanthesis].strip()

    return randomWord

if __name__ == '__main__':
    print pickWordAtRandom()
