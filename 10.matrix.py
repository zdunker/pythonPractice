aArrayRow1 = [4,56,2]
aArrayRow2 = [1,0,5]
aArrayRow3 = [5,7,8]
aArray = [aArrayRow1,aArrayRow2,aArrayRow3]

bArrayCol1 = [3,5,6]
bArrayCol2 = [5,1,1]
bArray = [bArrayCol1,bArrayCol2]

#first we need to calculate the format(size) of output matrix
cArrayX = len(bArray)
cArrayY = len(aArray)

cArray = []
for i in range(cArrayY):
    aArrayRow = aArray[i]
    thisRow = []
    for j in range(cArrayX):
        bArrayCol = bArray[j]
        sum = 0
        for k in range(len(aArrayRow)):
            sum += aArrayRow[k]*bArrayCol[k]
        thisRow.append(sum)
    cArray.append(thisRow)

print cArray