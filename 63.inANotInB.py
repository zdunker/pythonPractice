def inANotInB(aList, bList):
    retList = []
    for i in range(len(aList)):
        curAElement = aList[i]
        found = False
        for j in range(len(bList)):
            if curAElement == bList[j]:
                found = True
        if not found:
            retList.append(curAElement)
    
    return retList

if __name__ == "__main__":
    listA = ['Peter','Mian','Chris','Dwight']
    listB = ['JoeC','JoeZ','Hubert','Peter','Mian']
    listAOnly = inANotInB(listA, listB)
    for comp in listAOnly:
        print comp