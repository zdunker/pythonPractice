def commonString(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    
    commonList = []
    
    for i in range(len1):
        for j in range(len2):
            if str1[i] == str2[j]:
                match = whatever(str1, str2, i, j)
                if match not in commonList:
                    commonList.append(match)
    
    return commonList
                
def whatever(str1,str2, i, j,match = ''):
    if str1[i] == str2[j]:
        match += str1[i]
        if i+1 < len(str1) and j+1 < len(str2):
            #print match
            return whatever(str1, str2, i+1, j+1, match)
        else:
            return match
    else:
        return match

if __name__ == "__main__":
    list = commonString('decfaxfalist', 'cccecccfalist')
    print list