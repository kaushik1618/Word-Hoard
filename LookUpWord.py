#!/usr/bin/env python

def getDefinition(word="ERROR"):

    import time, subprocess

    dictProcess = subprocess.Popen(["dict", word], stdout=subprocess.PIPE)
    #time.sleep(5)  #not required for offline dict sources
    definition = dictProcess.stdout.read()

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
