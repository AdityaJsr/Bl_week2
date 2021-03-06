"""
Title - Write a Python program to count occurrences of a substring in a string.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 

def countSubString():
    str1 = input("Enter the main string : ")
    key = input("Enter the key value you want to count : ")
    print(str1.count(key))

if __name__ == "__main__":
    countSubString()

