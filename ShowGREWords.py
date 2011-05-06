#!/usr/bin/env python

def loopThroughGREWords(wordsFileOrDir):

    import os, time, ReadWordList, LookUpWord, PanelNotification

    pidFile = '/home/kaushikk/GREWords.txt'
    pidFileHandle = open(pidFile,'wb')
    pidFileHandle.write("%s" % os.getpid())
    pidFileHandle.close()

    noteStartTime = 0

    while(True):
        word = ReadWordList.pickWordAtRandom(wordsFileOrDir)
        definition = LookUpWord.getDefinition(word)

        while(time.time()-noteStartTime < 11):
            time.sleep(1)

        noteStartTime = time.time()
        PanelNotification.showPanelNotification(word, definition)
    
if __name__ == '__main__':
    loopThroughGREWords('/home/kaushikk/Documents/GRE/Barrons/Wordlist/New Words/')
