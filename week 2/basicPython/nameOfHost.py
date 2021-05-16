"""
Title - Write a Python program to get the name of the host on which the routine is running.
Author name - Aditya Kumar
Ceation time - ‎‎02 ‎March ‎2021 ‏‎
Modified time - ‎‎‎02 ‎March ‎2021‎

"""


import socket

def getSocketName():
    host_name = socket.gethostname()
    print("Host name:", host_name)

if __name__ == '__main__':
    getSocketName()