#!/usr/bin/env python
import os, sys, time, subprocess, ReadWordList, LookUpWord, PanelNotification
timeStringFormat = "%A, %d %B %Y, %I:%M:%S %p"

def loopThroughGREWords(wordsFileOrDir, tempOutFile):
    print "%s - Started logging...\n" % time.strftime(timeStringFormat)
    noteStartTime = 0
    while(True):
        word = ReadWordList.pickWordAtRandom(wordsFileOrDir)
        definition = LookUpWord.getDefinition(word, tempOutFile)
        while(time.time()-noteStartTime < 11):
            time.sleep(1)
        noteStartTime = time.time()
        PanelNotification.showPanelNotification(word, definition)

def getPIDFromFile(pidFile):
    if os.path.exists(pidFile) and os.path.isfile(pidFile):
        pidFileHandle = open(pidFile, 'rb')
        pid = pidFileHandle.read()
        pidFileHandle.close()
        return pid
    else:
        return -1

def processWithPIDHasName(pid, processName):
    subprocessHandle = subprocess.Popen(['ps', '-p', pid, '-O', 'c'], stdout=subprocess.PIPE)
    output = subprocessHandle.stdout.read()
    pos = output.find(processName)
    if pos >= 0:
        return True
    else:
        return False

def deleteFiles(filesList):
    for filePath in filesList:
        if os.path.exists(filePath) and os.path.isfile(filePath):
            os.remove(filePath)
    return

def writePIDToFile(pidFile):
    pidFileHandle = open(pidFile,'wb')
    pidFileHandle.write("%s" % os.getpid())
    pidFileHandle.close()
    return

def redirectStdOutAndStdErrToFile(logFile):
    logFileHandle = open(logFile, 'wb', 0)                          # 0 is for unbuffered
    sys.stdout = logFileHandle
    sys.stderr = logFileHandle
    return

if __name__ == '__main__':
    srcDir = os.path.split(PanelNotification.__file__)[0]
    pidFile = os.path.join(srcDir, 'Word-Hoard.pid')
    logFile = os.path.join(srcDir, 'Word-Hoard.log')
    tempOutFile = os.path.join(srcDir, 'Word-Hoard-Definition.txt')
    pid = getPIDFromFile(pidFile)
    if pid > 0 and processWithPIDHasName(pid, 'ShowWords.py'):
        subprocess.Popen(['kill', pid])
        deleteFiles([pidFile, logFile])
        sys.exit(1)
    else:
        writePIDToFile(pidFile)
        redirectStdOutAndStdErrToFile(logFile)
        loopThroughGREWords('/home/kaushikk/Documents/GRE/Barrons/Wordlist/New Words/', tempOutFile)

# Yet to handle closing logFileHandle gracefully
