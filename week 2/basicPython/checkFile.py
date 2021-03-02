'''
Write a Python program to check whether a file exists

'''
import os.path

def fileExists():
    path = '"D:/vs studio/bridgeLabz/week2/week 2/basicPython/checkFile.py"'
    if(os.path.isfile(path)):
    # os.path.isfile(path)
        print(True)
    else:
        print(False)
if __name__ ==  "__main__":
    fileExists()