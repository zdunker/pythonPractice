def recur(charMatrix,i,j,tarCountry,curPattern=''):
    if not curPattern in tarCountry:
        return
    if curPattern == tarCountry:
        print curPattern
        return
    if i+1 in charMatrix.keys():
        if j+1 < len(charMatrix[i+1]):
            recur(charMatrix,i+1,j+1,tarCountry,curPattern+charMatrix[i+1][j+1])
        if j-1 >= 0:
            recur(charMatrix, i+1, j-1, tarCountry, curPattern+charMatrix[i+1][j-1])
        recur(charMatrix, i+1, j, tarCountry, curPattern+charMatrix[i+1][j])
    if i-1 in charMatrix.keys():
        if j+1 < len(charMatrix[i-1]):
            recur(charMatrix,i-1,j+1,tarCountry,curPattern+charMatrix[i-1][j+1])
        if j-1 >= 0:
            recur(charMatrix, i-1, j-1, tarCountry, curPattern+charMatrix[i-1][j-1])
        recur(charMatrix, i-1, j, tarCountry, curPattern+charMatrix[i-1][j])
    if j+1 < len(charMatrix[i]):
        recur(charMatrix,i,j+1,tarCountry,curPattern+charMatrix[i][j+1])
    if j-1 >= 0:
        recur(charMatrix, i, j-1, tarCountry, curPattern+charMatrix[i][j-1])

def recur1(charMatrix,i,j,tarCountry,curPattern=''):
    if not curPattern in tarCountry:
        return
    if curPattern == tarCountry:
        print curPattern
        return
    if i+1 in charMatrix.keys():
        if j+1 < len(charMatrix[i+1]):
                recur1(charMatrix,i+1,j+1,tarCountry,curPattern+charMatrix[i+1][j+1])
        else:
            return
    return

def recur2(charMatrix,i,j,tarCountry,curPattern=''):
    if not curPattern in tarCountry:
        return
    if curPattern == tarCountry:
        print curPattern
        return
    if i+1 in charMatrix.keys():
        if j-1 >= 0:
            recur2(charMatrix, i+1, j-1, tarCountry, curPattern+charMatrix[i+1][j-1])
        else:
            return
    return

def recur3(charMatrix,i,j,tarCountry,curPattern=''):
    if not curPattern in tarCountry:
        return
    if curPattern == tarCountry:
        print curPattern
        return
    if i+1 in charMatrix.keys():
        recur3(charMatrix, i+1, j, tarCountry, curPattern+charMatrix[i+1][j])
    return

def recur4(charMatrix,i,j,tarCountry,curPattern=''):
    if not curPattern in tarCountry:
        return
    if curPattern == tarCountry:
        print curPattern
        return
    if i-1 in charMatrix.keys():
        if j+1 < len(charMatrix[i-1]):
                recur4(charMatrix,i-1,j+1,tarCountry,curPattern+charMatrix[i-1][j+1])
        else:
            return
    return

def recur5(charMatrix,i,j,tarCountry,curPattern=''):
    if not curPattern in tarCountry:
        return
    if curPattern == tarCountry:
        print curPattern
        return
    if i-1 in charMatrix.keys():
        if j-1 >= 0:
            recur5(charMatrix, i-1, j-1, tarCountry, curPattern+charMatrix[i-1][j-1])
        else:
            return
    return

def recur6(charMatrix,i,j,tarCountry,curPattern=''):
    if not curPattern in tarCountry:
        return
    if curPattern == tarCountry:
        print curPattern
        return
    if i-1 in charMatrix.keys():
        recur6(charMatrix, i-1, j, tarCountry, curPattern+charMatrix[i-1][j])
    return

def recur7(charMatrix,i,j,tarCountry,curPattern=''):
    if not curPattern in tarCountry:
        return
    if curPattern == tarCountry:
        print curPattern
        return
    if j+1 < len(charMatrix[i]):
        recur7(charMatrix,i,j+1,tarCountry,curPattern+charMatrix[i][j+1])
    return

def recur8(charMatrix,i,j,tarCountry,curPattern=''):
    if not curPattern in tarCountry:
        return
    if curPattern == tarCountry:
        print curPattern
        return
    if j-1 >= 0:
        recur8(charMatrix,i,j-1,tarCountry,curPattern+charMatrix[i][j-1])
    return

if __name__ =='__main__':
    charMatrix = {}
    charMatrix[0] = ['F','Y','Y','H','N','R','D']
    charMatrix[1] = ['R','L','J','C','I','N','U']
    charMatrix[2] = ['A','A','W','A','A','H','R']
    charMatrix[3] = ['N','T','K','L','P','N','E']
    charMatrix[4] = ['C','I','L','F','S','A','P']
    charMatrix[5] = ['E','O','G','O','T','P','N']
    charMatrix[6] = ['H','P','O','L','A','N','D']
    tarCountries = ['FRANCE','ITALY','SPAIN','PERU','HOLLAND','JAPAN','TOGO','POLAND']
    for tarCountry in tarCountries:
        for i in charMatrix.keys():
            for j in range(len(charMatrix[i])):
                if charMatrix[i][j] == tarCountry[0]:
                    recur1(charMatrix, i, j, tarCountry,charMatrix[i][j])
                    recur2(charMatrix, i, j, tarCountry,charMatrix[i][j])
                    recur3(charMatrix, i, j, tarCountry,charMatrix[i][j])
                    recur4(charMatrix, i, j, tarCountry,charMatrix[i][j])
                    recur5(charMatrix, i, j, tarCountry,charMatrix[i][j])
                    recur6(charMatrix, i, j, tarCountry,charMatrix[i][j])
                    recur7(charMatrix, i, j, tarCountry,charMatrix[i][j])
                    recur8(charMatrix, i, j, tarCountry,charMatrix[i][j])
                    