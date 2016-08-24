def iterFac(n):
    """n!"""
    retVal = 1
    for i in range(1,n+1):
        retVal*= i
    return retVal

def recurFac(n):
    if n == 1:
        return 1
    return n*recurFac(n-1)

if __name__ == "__main__":
    print iterFac(4)
    print recurFac(4)