import time

def isPrime(num, x):
    if num % x != 0:
        if x <= 2:
            return True
        else:
            return isPrime(num, x-1)
    else:
        return False

def listPrime(n):
    primeList = []
    for i in range(2,n):
        if isPrime(i, i-1):
            primeList.append(i)
    return primeList

def alterPrimeList(n):
    primeDict = {}
    primeList = []
    for i in range(2,n+1):
        primeDict[i] = True
    
    index = 2
    while index <= n:
        if primeDict[index]:
            tmp = index*2
            while tmp < n:
                primeDict[tmp] = False
                tmp += index
        index += 1
    
    for i in range(2,n+1):
        if primeDict[i]:
            primeList.append(i)
    return primeList

if __name__ == "__main__":
    startTime1 = time.time()
    list1 = alterPrimeList(400)
    print time.time() - startTime1
    startTime2 = time.time()
    list2 = listPrime(400)
    print time.time() - startTime2