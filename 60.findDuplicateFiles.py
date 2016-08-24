import os
import hashlib

def getDuplicateFile(rootDir):
    fileList = []
    fileMd5Dict = {}
    duplicatedFileList = []
    
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            fileList.append(os.path.join(root,file))
    for file in fileList:
        with open(file,'rb') as rf:
            md5sum = hashlib.md5(rf.read()).hexdigest()
            if md5sum in fileMd5Dict.values():
                duplicatedFileList.append(file)
                #also have to push original file to list
                for file1 in fileMd5Dict.keys():
                    if fileMd5Dict[file1] == md5sum and file1 not in duplicatedFileList:
                        duplicatedFileList.append(file1)
            fileMd5Dict[file] = md5sum
    
    return duplicatedFileList

if __name__ == "__main__":
    rootDir = 'C:\\test_area\\'
    list = getDuplicateFile(rootDir)
    for file in list:
        print file