import random
def shuffleList(cardList):
    if len(cardList) ==1:
        return [cardList[0]]
    i = random.randint(0,len(cardList)-1)
    return shuffleList(cardList[0:i]+cardList[i+1:])+[cardList[i]]

if __name__ == '__main__':
    cardList = ['13','32','13','43','6','34','62','18']
    newList = shuffleList(cardList)
    print newList