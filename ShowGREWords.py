#!/usr/bin/env python

def loopThroughGREWords(wordsFileOrDir):

    import time, ReadWordList, LookUpWord, PanelNotification

    noteStartTime = 0

    while(True):
        word = ReadWordList.pickWordAtRandom(wordsFileOrDir)
        definition = LookUpWord.getDefinition(word)

        while(time.time()-noteStartTime < 11):
            time.sleep(1)

        noteStartTime = time.time()
        PanelNotification.showPanelNotification(word, definition)
    
if __name__ == '__main__':
    loopThroughGREWords('/home/kaushikk/Documents/GRE/Barrons/Wordlist/New Words')
