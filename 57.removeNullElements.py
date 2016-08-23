aList = ['','sadf','ece','',None,None,3,'ds']
print aList
"""
def isTrue(x):
    if x:
        return 1
    else:
        return 0

aList = filter(isTrue, aList)
print aList"""
aList = [var for var in aList if var]
print aList