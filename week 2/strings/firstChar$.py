"""
Title - Write a Python program to get a string from a given string where all occurrences of its
        first char have been changed to '$', except the first char itself.
        Sample String : 'restart'
        Expected Result : 'resta$t'
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 

def changeChar():
    str1 = input("Enter the input string : ")
    char = str1[0]
    str1 = str1.replace(char,'$')
    str1 = char + str1[1:]
    print(str1)

if __name__ == "__main__":
    changeChar() 


