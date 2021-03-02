"""
Title - Write a Python program to find out the number of CPUs using.
Author name - Aditya Kumar
Ceation time - ‎‎02 ‎March ‎2021 ‏‎
Modified time - ‎‎‎02 ‎March ‎2021‎

"""

import multiprocessing

def numOfCpu():
    print(multiprocessing.cpu_count())

if __name__ == '__main__':
    numOfCpu()