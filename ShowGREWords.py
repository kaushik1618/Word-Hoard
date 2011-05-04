#!/usr/bin/env python

def loopThroughGREWords(wordsFileOrDir, notificationTimeoutInSecs):

    import ReadWordList, PanelNotification

    word = ReadWordList.pickWordAtRandom(wordsFileOrDir)
    definition = "not implemented yet"
    PanelNotification.showPanelNotification(word, definition, notificationTimeoutInSecs)
    
if __name__ == '__main__':
    loopThroughGREWords('/home/kaushikk/Documents/GRE/Barrons/Wordlist/New Words', 5)
