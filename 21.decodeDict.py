from networkx.algorithms.centrality.degree_alg import out_degree_centrality
expInput = 'xlmt mt pf ryxvakrqz gbf ipkr'
expOutput = 'this is an extremely fun game'

decodeDict = {}
for i in range(len(expInput)):
    decodeDict[expInput[i]] = expOutput[i]

myInput = 'xlmt mt pf ryxvakrqz gbf ipkr'
myOutput = ''
for i in range(len(myInput)):
    if myInput[i] in decodeDict.keys():
        myOutput += decodeDict[myInput[i]]
    else:
        myOutput += myInput[i]

print myOutput