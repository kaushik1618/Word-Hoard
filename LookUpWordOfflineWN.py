#!/usr/bin/env python

def getDefinition(word="ERROR"):

    import time, subprocess

    dictOpts = ["-synsn", "-synsv", "-synsa", "-synsr", "-simsv"]
    definition = ""
    
    for dictOpt in dictOpts:
        dictProcess = subprocess.Popen(["wn", word, dictOpt], stdout=subprocess.PIPE)
        definition = dictProcess.stdout.read()
        if definition != "":
            break

    definitionLines = definition.split('\n')
    truncatedDefinition = []

    for line in definitionLines:
        if not line.startswith('Synonyms/Hypernyms') and line.find('sense of')==-1 and line.find('senses of')==-1 and len(line.strip())>0:
            truncatedDefinition.append(line.strip())

    definition = '\n'.join(truncatedDefinition)

    return definition.strip()
    
if __name__ == '__main__':
    print "'%s'" % getDefinition("decimate")
