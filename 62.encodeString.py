def encodeString(encStr):
    curChar =''
    curCharNum = 0
    retStr = ''
    for i in range(len(encStr)):
        if curChar!=encStr[i]:
            if curCharNum!=0:
                retStr += curChar
                retStr += str(curCharNum)
                curCharNum = 0
            curChar = encStr[i]
        curCharNum +=1
    retStr += curChar
    retStr += str(curCharNum)
    return retStr

if __name__ == '__main__':
    print encodeString('aabbaadddc')