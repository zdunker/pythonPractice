def getPermutation(s, prefix=''):
    if len(s) == 0:
        print prefix
    for i in range(len(s)):
        print i
        print s[0:i]+s[i+1:len(s)]
        getPermutation(s[0:i]+s[i+1:len(s)],prefix+s[i] )

getPermutation('aabcd')
################################################
#One chosen char and the rest
#To traverse every single char in the rest is the target