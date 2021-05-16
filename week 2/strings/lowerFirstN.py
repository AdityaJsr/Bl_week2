"""
Title - Write a Python program to lowercase first n characters in a string.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 

def lowerN():
    str1 = input("Enter the main string  : ")
    n = int(input("enter the nth index : "))
    print(str1[:n].lower() + str1[n:])

if __name__ == "__main__":
    lowerN()