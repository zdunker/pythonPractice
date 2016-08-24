def getMultipleSum(limit,tar1,tar2):
    numDict = {}
    for i in range(2, limit+1):
        numDict[i] = False
    for i in range(0, limit+1, tar1):
        numDict[i] = True
    for i in range(0, limit+1, tar2):
        numDict[i] = True
    sum = 0
    for i in numDict.keys():
        if numDict[i]:
            sum+= i
    return sum

if __name__ == "__main__":
    print getMultipleSum(10, 3, 5)