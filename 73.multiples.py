def getMultipleSum(limit,tar1,tar2):
    numDict = {}
    for i in range(2, limit+1):
        numDict[i] = False
    
    i=tar1
    while i<limit:
        numDict[i] = True
        i+=tar1
    i=tar2
    while i<limit:
        numDict[tar2] = True
        i+=tar2
    
    sum = 0
    for i in numDict.keys():
        if numDict[i]:
            sum+= i
    return sum

if __name__ == "__main__":
    print getMultipleSum(1000, 3, 5)