openList = ['(','[','{']
closeList = [')',']','}']

def areMatched(char1, char2):
    if char1 == '(' and char2 == ')':
        return True
    elif char1 == '[' and char2 == ']':
        return True
    elif char1 == '{' and char2 == '}':
        return True
    else:
        return False

def isOpen(char):
    if char in openList:
        return True
    return False

def isClose(char):
    if char in closeList:
        return True
    return False

def checkBalance(input):
    stack = []
    i=0
    for i in range(len(input)):
        if not isOpen(input[i]) and not isClose(input[i]):
            pass
        elif isOpen(input[i]):
            stack += [input[i]]
        elif isClose(input[i]):
            if len(stack) != 0:
                if not areMatched(stack[-1], input[i]):
                    return False
                else:
                    stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = 'foo{}()[]'
    str2 = '[}'
    str3 = '{}'
    if checkBalance(str3):
        print "yes"