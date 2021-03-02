'''
Write a Python program to get the current username

'''


import getpass

def checkUser():
    print(getpass.getuser())

if __name__ == '__main__':
    checkUser()