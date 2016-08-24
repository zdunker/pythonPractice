str1 = 'brattle'
str2 = 'mettlesome'

retList = []

for i in range(len(str1)):
    for j in range(len(str2)):
        match = ''
        tempi = i
        tempj = j
        while tempi < len(str1) and tempj < len(str2) and str1[tempi] == str2[tempj]:
            match += str1[tempi]
            tempi += 1
            tempj += 1
        if match:
            retList.append(match)

maxLen = 0
for comp in retList:
    if len(comp)> maxLen:
        maxComp = comp
        maxLen = len(comp)

print maxComp