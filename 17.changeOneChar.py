import sys

#first filter out words with same length
def firstFilter(wordList, targetWord):
    tarLen = len(targetWord)
    returnList = []
    for word in wordList:
        if len(word) == tarLen:
            returnList.append(word)
    return returnList

#for each word recursive?
def scanWord(wordList,targetWord):
    returnList = []
    for word in wordList:
        numOfSame = 0
        numOfDiff = 0
        for i in range(len(word)):
            if word[i] == targetWord[i]:
                numOfSame += 1
            else:
                numOfDiff += 1
        if numOfDiff == 1:
            returnList.append(word)
    return returnList

if __name__ == "__main__":
    wordList = ['bar','cat','can','jar','sat','rat','mat','hudson']
    targetWord = 'jar'
    newWordList = firstFilter(wordList, targetWord)
    new2WordList = scanWord(newWordList, targetWord)
    print new2WordList