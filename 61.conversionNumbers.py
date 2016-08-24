import math

def decToBin(n):
    bin = []
    while n>=1:
        bin.append(str(n%2))
        n = n/2
    bin.reverse()
    return ''.join(bin)

def binToDec(n):
    dec = 0
    fac = 0
    while n > 0:
        dec += (n%10)* math.pow(2, fac)
        fac+=1
        n = n/10
    return int(dec)

def decToOct(n):
    oct = []
    while n>=1:
        oct.append(str(n%8))
        n = n/8
    oct.reverse()
    return ''.join(oct)

def octToDec(n):
    dec = 0
    fac = 0
    while n>0:
        dec += (n%10)*math.pow(8, fac)
        fac+=1
        n=n/10
    return int(dec)

hexDigitDict = {}
hexDigitDict[0] = '0'
hexDigitDict[1] = '1'
hexDigitDict[2] = '2'
hexDigitDict[3] = '3'
hexDigitDict[4] = '4'
hexDigitDict[5] = '5'
hexDigitDict[6] = '6'
hexDigitDict[7] = '7'
hexDigitDict[8] = '8'
hexDigitDict[9] = '9'
hexDigitDict[10] = 'a'
hexDigitDict[11] = 'b'
hexDigitDict[12] = 'c'
hexDigitDict[13] = 'd'
hexDigitDict[14] = 'e'
hexDigitDict[15] = 'f'

def decToHex(n):
    global hexDigitDict
    hex = []
    while n >0:
        hex.append(hexDigitDict[n%16])
        n = n/16
    hex.reverse()
    return ''.join(hex)

def hexToDec(n):
    global hexDigitDict
    dec = 0
    fac = len(n)-1
    hex = n
    hexDigits = []
    for i in range(len(n)):
        dec += hexDigitDict.keys()[hexDigitDict.values().index(n[i])] * math.pow(16, fac)
        fac -= 1
        
    return int(dec)

if __name__ == "__main__":
    print decToBin(133)
    print binToDec(1101)
    print decToOct(64)
    print octToDec(1420)
    print decToHex(16)
    print hexToDec('7a')