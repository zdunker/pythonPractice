intArray = [10,11,12,13]

retArray = []
for firstPtr in range(len(intArray)):
    i = 1
    for secondPtr in range(len(intArray)):
        if not secondPtr == firstPtr:
            i = i*intArray[secondPtr]
    retArray.append(i)

for num in retArray:
    print num