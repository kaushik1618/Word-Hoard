#!/usr/bin/env python

def getDefinition(word="ERROR"):

    import time, os, subprocess

    outFile = "/home/kaushikk/GREDefinition.txt"
    outFileHandle = open(outFile, 'wb')
    dictProcess = subprocess.Popen(["dict", word], stdout=outFileHandle)
    outFileHandle.close()

    time.sleep(1)  #required for output to be written to file before reading

    outFileHandle = open(outFile, 'rb')
    definition = outFileHandle.read()
    outFileHandle.close()

    os.remove(outFile)

    position = definition.find("From WordNet")

    if position < 0:
        definition = "Not found in WordNet 3.0"
        return definition

    else:
        definition = definition[position:]
        position = definition.lower().find(word.lower())
        definition = definition[position:]
        position = definition.find("From ")

        if position >= 0:
            definition = definition[:position]

    return definition[len(word):].strip()

if __name__ == '__main__':
    print getDefinition()
