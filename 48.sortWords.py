def merge(wordList, left, right):
    midl = (left + right)/2
    if left < right:
        merge(wordList, left, midl)
        merge(wordList, midl+1, right)
        mergeSort(wordList,left,midl,right)

def mergeSort(wordList, left, midl, right):
    leftPtr = left
    rightPtr = midl
    retList = []
    while leftPtr < midl and rightPtr < right +1 :
        if wordList[leftPtr] < wordList[rightPtr]:
            retList.append(wordList[leftPtr])
            leftPtr += 1
        if wordList[rightPtr] < wordList[leftPtr]:
            retList.append(wordList[rightPtr])
            rightPtr += 1
    while leftPtr < midl:
        retList.append(wordList[leftPtr])
        leftPtr += 1
    while rightPtr < right+1:
        retList.append(wordList[rightPtr])
        rightPtr += 1
    tmp = 0
    for i in range(left,right+1):
        wordList[i] = retList[tmp]
        tmp += 1

if __name__ == '__main__':
    wordList = ['a','','das','sfs','fs','fee','sdas','asg']
    merge(wordList, 0, len(wordList)-1)
    for word in wordList:
        print word