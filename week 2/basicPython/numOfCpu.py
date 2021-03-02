'''
Write a Python program to find out the number of CPUs using

''' 

import multiprocessing

def numOfCpu():
    print(multiprocessing.cpu_count())

if __name__ == '__main__':
    numOfCpu()