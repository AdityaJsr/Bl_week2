"""
Title - Write a Python program to retrieve file properties.
Author name - Aditya Kumar
Creation time - ‎‎02 ‎March ‎2021
Modified time - ‎‎‎02 ‎March ‎2021‏‎

"""
import os.path
import time

def fileProp():
    print('File         :', "D:/music/29th jan/(05) - Zedd - Done With Love.mp3")
    print('Access time  :', time.ctime(os.path.getatime("D:/music/29th jan/(05) - Zedd - Done With Love.mp3")))
    print('Modified time:', time.ctime(os.path.getmtime("D:/music/29th jan/(05) - Zedd - Done With Love.mp3")))
    print('Change time  :', time.ctime(os.path.getctime("D:/music/29th jan/(05) - Zedd - Done With Love.mp3")))
    print('Size         :', os.path.getsize("D:/music/29th jan/(05) - Zedd - Done With Love.mp3"))

if __name__ == "__main__":
    fileProp()