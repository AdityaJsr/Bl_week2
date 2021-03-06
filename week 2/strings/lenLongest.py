"""
Title - Write a Python function that takes a list of words and returns the length of the longestone.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 

def longestlen():
    string = input("Enter the input-string : ").split(' ')
    len1 = 0
    for words in string:
        if len(words)>(len1):
            len1 = len(words)
            
    print(len1)


if __name__ == "__main__":
    longestlen()