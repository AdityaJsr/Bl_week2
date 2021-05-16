"""
Title - Write a Python program to get the current username.
Author name - Aditya Kumar
Ceation time - ‎‎02 ‎March ‎2021 ‏‎
Modified time - ‎‎‎02 ‎March ‎2021‎

"""



import getpass

def checkUser():
    print(getpass.getuser())

if __name__ == '__main__':
    checkUser()