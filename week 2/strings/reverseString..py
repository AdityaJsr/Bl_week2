"""
Title - Write a Python program to reverse a string.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 
def revString():
    str1 = input("Enter the string you want to reverse : ")
    str1 = "".join(reversed(str1)) 
    print(str1)

if __name__ == "__main__":
    revString()