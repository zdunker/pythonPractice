import threading

readFile = 'WorldCompanyBigBoss.txt'

class textRW():
    def __init__(self, readFile = '', writeFile = '', prefix = ''):
        self.readFile = readFile
        self.writeFile = writeFile
        self.prefix = prefix
    
    def prefixFile(self,prefix = ''):
        if not prefix:
            prefix = self.prefix
        with open(self.readFile) as rf:
            content = rf.readlines()
        newContent = []
        for line in content:
            newContent.append(prefix + line)
        with open(self.writeFile,'a') as wf:
            for line in newContent:
                wf.write(line)
    
if __name__ == '__main__':
    trw = textRW('WorldCompanyBigBoss.txt','pei.txt',prefix = 'lol')
    
    t1 = threading.Thread(target=textRW.prefixFile, args=(trw,str(1)+str(1)+str(1)))
    t2 = threading.Thread(target=textRW.prefixFile, args=(trw,str(2)+str(2)+str(2)))
    t3 = threading.Thread(target=textRW.prefixFile, args=(trw,str(3)+str(3)+str(3)))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()