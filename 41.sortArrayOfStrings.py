def mergeSort(strList,left,right):
    midl = (left+right)/2
    if left < right:
        mergeSort(strList, left, midl)
        mergeSort(strList, midl+1, right)
        merge(strList, left,midl,right)

def merge(strList,left,midl,right):
    leftPtr = left
    rightPtr = midl+1
    retList = []
    while leftPtr <= midl and rightPtr < right+1:
        if strList[rightPtr] < strList[leftPtr]:
            retList.append(strList[leftPtr])
            leftPtr+=1
        if strList[leftPtr] <= strList[rightPtr]:
            retList.append(strList[rightPtr])
            rightPtr+=1
    while leftPtr <= midl:
        retList.append(strList[leftPtr])
        leftPtr += 1
    while rightPtr < right+1:
        retList.append(strList[rightPtr])
        rightPtr += 1
    
    tmp = 0
    for i in range(left,right+1):
        strList[i] = retList[tmp]
        tmp+=1

if __name__ == '__main__':
    strList = ['hello','how','are','you','hello','zoey','yaho']
    mergeSort(strList, 0, len(strList)-1)
    for str in strList:
        print str