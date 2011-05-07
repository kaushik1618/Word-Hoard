#!/usr/bin/env python

import os, sys, time, ReadWordList, LookUpWord, PanelNotification

timeStringFormat = "%A, %d %B %Y, %I:%M:%S %p"

def loopThroughGREWords(wordsFileOrDir):

    print "%s - Started logging...\n" % (time.strftime(timeStringFormat), )

    noteStartTime = 0

    while(True):
        word = ReadWordList.pickWordAtRandom(wordsFileOrDir)
        definition = LookUpWord.getDefinition(word)

        while(time.time()-noteStartTime < 11):
            time.sleep(1)

        noteStartTime = time.time()
        PanelNotification.showPanelNotification(word, definition)
    
if __name__ == '__main__':

    pidFile = '/home/kaushikk/Word-Hoard.pid'
    pidFileHandle = open(pidFile,'wb')
    pidFileHandle.write("%s" % os.getpid())
    pidFileHandle.close()

    logFile = '/home/kaushikk/Word-Hoard.log'
    logFileHandle = open(logFile, 'wb', 0)                          # 0 is for unbuffered
    sys.stdout = logFileHandle
    sys.stderr = logFileHandle

    loopThroughGREWords('/home/kaushikk/Documents/GRE/Barrons/Wordlist/New Words/')

    logFileHandle.close()
