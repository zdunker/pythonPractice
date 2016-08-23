def reverseString(str):
    if len(str) <= 1:
        return str
    else:
        return reverseString(str[1:len(str)])+str[0]
    
if __name__ == '__main__':
    print reverseString('hellothere')