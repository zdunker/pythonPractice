import urllib2
import time

def wordDictNoMapReducer(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    wordDict = {}

    for line in response:
        wordlist = line.split()
        for word in wordlist:
            if word not in wordDict.keys():
                wordDict[word] = 1
            else:
                wordDict[word] += 1
    return wordDict


if __name__ == '__main__':
    url = 'http://sixty-north.com/c/t.txt'
    startTime = time.time()
    wordDict = wordDictNoMapReducer(url)
    print time.time() - startTime
    
    startTime = time.time()