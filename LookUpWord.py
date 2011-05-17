#!/usr/bin/env python

def getDefinition(word='ERROR', tempOutFile=None):
    import re, time, os, subprocess
    patternForNewLine = re.compile('^[a-z]{0,3} ?\d: ')   #patternForNewLine to determine where to insert newline (only at "1. ", "2. ", etc.)
    patternToRemoveExamples = re.compile('; ".*"')    #patternToRemoveExamples to remove examples within double quotes
    with open(tempOutFile, 'wb') as tempOutFileHandle:
        dictProcess = subprocess.Popen(["dict", word], stdout=tempOutFileHandle)
    time.sleep(1)  #required for output to be written to file before reading
    with open(tempOutFile, 'rb') as tempOutFileHandle:
        definition = tempOutFileHandle.read()
    os.remove(tempOutFile)
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
    definition = definition[len(word):].strip()
    lines = definition.split('\n')
    definition = lines[0].strip()
    for lineNumber in range(1, len(lines)):
        if re.search(patternForNewLine, lines[lineNumber].strip()):
            delimiter = '\n'
        else:
            delimiter = ' '
        definition = delimiter.join([definition, lines[lineNumber].strip()])
    definition = re.sub(patternToRemoveExamples, '', definition)
    return definition

if __name__ == '__main__':
    print getDefinition('steep', 'chumma')
