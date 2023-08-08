def encode(txt, finalStr=""):

    for i in txt:

        finalStr = finalStr + r"\x" + format(ord(i), "x")

    return finalStr

def decode(txt, finalStr=""):

    wordList = txt.split('\\')
    wordList.remove('')

    i = 0
    while i < len(wordList):
        x = wordList[i]
        wordList[i] = x[1:]
        x = wordList[i]
        wordList[i] = int(wordList[i], base=16)
        i += 1

    for i in wordList:
        finalStr = finalStr + chr(i)

    return finalStr