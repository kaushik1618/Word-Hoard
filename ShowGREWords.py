#!/usr/bin/env python

def loopThroughGREWords(wordsFileOrDir):

    import os, time, ReadWordList, LookUpWordOfflineWN, PanelNotification

    selfPID = os.getpid()
    pidFile = open('/home/kaushikk/GREWords.txt','wb')
    pidFile.write("%s" % selfPID)
    pidFile.close()

    noteStartTime = 0

    while(True):
        word = ReadWordList.pickWordAtRandom(wordsFileOrDir)
        definition = LookUpWordOfflineWN.getDefinition(word)

        while(time.time()-noteStartTime < 11):
            time.sleep(1)

        noteStartTime = time.time()
        PanelNotification.showPanelNotification(word, definition)
    
if __name__ == '__main__':
    loopThroughGREWords('/home/kaushikk/Documents/GRE/Barrons/Wordlist/New Words')
