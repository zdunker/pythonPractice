import os
import sys


def recursDir(directory, targetDir):
    subDirList = os.listdir(directory)
    for subDir in subDirList:
        if os.path.isdir(os.path.join(directory,subDir)):
            recursDir(os.path.join(directory,subDir), os.path.join(targetDir,subDir))
        else:
            if not os.path.isdir(targetDir):
                batch = b"""\
                md %s
                """%(targetDir)
                os.system(batch)
            batch = b"""\
            copy %s %s
            """%(os.path.join(directory,subDir), targetDir)
            os.system(batch)
            print batch

if __name__ == "__main__":
    root = sys.argv[1]
    targetDir = sys.argv[2]
    recursDir(root, targetDir)