import sys

class Person():
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death

if __name__ == "__main__":
    pList = [Person(1900,1960),Person(1910,1950),Person(1920,1975),Person(1915,1980)]
    startY = int(sys.argv[1])
    endY = int(sys.argv[2])
    outputNum = 0
    for person in pList:
        if person.birth<startY and person.death>endY:
            outputNum += 1
    print outputNum