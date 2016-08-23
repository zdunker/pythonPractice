charDict = {}
charDict[0] = ['A','L','C','D']
charDict[1] = ['L','D','E','R']
charDict[2] = ['O','C','H','T']
charDict[3] = ['B','R','X','A']

def recur(charDict, tarWord, i, j, curWord = ''):
    if not curWord in tarWord:
        return
    if curWord == tarWord:
        print curWord
        return
    #below are those under right track
    if i+1 in charDict.keys():
        if j+1 < len(charDict[i]):
            recur(charDict, tarWord, i+1, j+1, curWord+charDict[i+1][j+1])
        if j-1 >= 0:
            recur(charDict, tarWord, i+1, j-1, curWord+charDict[i+1][j-1])
        recur(charDict, tarWord, i+1, j, curWord+charDict[i+1][j])
    if i-1 in charDict.keys():
        if j+1 < len(charDict[i]):
            recur(charDict, tarWord, i-1, j+1, curWord+charDict[i-1][j+1])
        if j-1 >= 0:
            recur(charDict, tarWord, i-1, j-1, curWord+charDict[i-1][j-1])
        recur(charDict, tarWord, i-1, j, curWord+charDict[i-1][j])
    if j+1 <len(charDict[i]):
        recur(charDict, tarWord, i, j+1, curWord+charDict[i][j+1])
    if j-1 >= 0:
        recur(charDict, tarWord, i, j-1, curWord+charDict[i][j-1])

if __name__ == '__main__':
    tarWord = 'HELLO'
    for i in charDict.keys():
        for j in range(len(charDict[i])):
            if charDict[i][j] == tarWord[0]:
                recur(charDict,tarWord,i,j,tarWord[0])               
    