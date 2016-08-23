from multiprocessing import Queue
import threading
import os

with open('WorldCompanyBigBoss.txt') as rf:
    content = rf.readlines()

firstHalfContent = content[:len(content)/2+1]
secondHalfContent = content[len(content)/2+1:]

os.system('del threadingWrite.txt')

def printContent(content):
    lock = threading.RLock()
    for line in content:
        print line
        with lock:
            wf = open('threadingWrite.txt','a')
            wf.write(line)
        
t1 = threading.Thread(target=printContent,args=(firstHalfContent,))
t2 = threading.Thread(target=printContent,args=(secondHalfContent,))
t1.start()
t2.start()
t1.join()
t2.join()