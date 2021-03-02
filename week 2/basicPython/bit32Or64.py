"""
Title - Write a Python program to determine if the python shell is executing in 32bit or 64bit mode.
on operating system.
Author name - Aditya Kumar
Ceation time - ‎‎02 ‎March ‎2021 ‏‎
Modified time - ‎‎‎02 ‎March ‎2021‎

"""

# For 32 bit it will return 32 and for 64 bit it will return 64
import struct

def printBit():
    print(struct.calcsize("P") * 8)

if __name__ == "__main__":
    printBit()