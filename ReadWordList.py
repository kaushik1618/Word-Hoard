#!/usr/bin/env python

def pickWordAtRandom(pathToFileOrDir=None):

    import sys, os, os.path, random

    if not os.path.exists(pathToFileOrDir):
        print "Path '%s' does not exist" % pathToFileOrDir
        sys.exit(1)

    if os.path.isdir(pathToFileOrDir):
        filesList = os.listdir(pathToFileOrDir)
        randomIndex = random.randrange(len(filesList))
        filePath = os.path.join(pathToFileOrDir, filesList[randomIndex])

    if os.path.isfile(pathToFileOrDir):
        filePath = pathToFileOrDir

    filePointer = open(filePath, 'rb')
    linesList = filePointer.readlines()
    filePointer.close()

    randomIndex = random.randrange(len(linesList))
    randomLine = linesList[randomIndex]
    randomWord = randomLine.replace('\n','')

    indexOfParanthesis = randomWord.find('(')

    if indexOfParanthesis>0:
        randomWord = randomWord[:indexOfParanthesis].strip()

    return randomWord

if __name__ == '__main__':
    print pickWordAtRandom()
