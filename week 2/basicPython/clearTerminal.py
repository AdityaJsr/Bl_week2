"""
Title - Write a Python program to clear terminal.
Author name - Aditya Kumar
Creation time - ‎‎02 ‎March ‎2021
Modified time - ‎‎‎02 ‎March ‎2021‏‎

"""
import os
import time

def clearTerminal():
    os.system("cls")
    time.sleep(2)

if __name__ == '__main__':
    clearTerminal()