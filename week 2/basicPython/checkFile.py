"""
Title - Write a Python program to check whether a file exists.
Author name - Aditya Kumar
Creation time - ‎‎02 ‎March ‎2021
Modified time - ‎‎‎02 ‎March ‎2021‏‎

"""

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