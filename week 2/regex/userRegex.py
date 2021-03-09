'''
Title - User Registration System matches user's First, last name EmailID,
        phoneNum, Password. with regEx pattern.
Author name - Aditya Kumar
Ceation time - ‎‎08 ‎March ‎2021 ‏‎
Modified time - ‎‎‎08 ‎March ‎2021‎

'''


import re
import getpass

def fName():
    FirstName = input("Enter the First name : ")
    pattern = '(^[A-Z][a-zA-Z]{2,})'
    match = re.match(pattern,FirstName)
    if match:
        print("True to the Pattern : ", match)
    else:
        print("Match Unsucessful : ")
        fName()

def lName():
    LastName = input("Enter the Last name : ")
    pattern = '(^[A-Z][a-zA-Z]{2,})'
    match = re.match(pattern,LastName)
    if match:
        print("True to the Pattern : ", match)
    else:
        print("Match Unsucessful : ")
        lName()

def eMail():
    Email = input("Enter your Email Id : ")
    pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    match = re.match(pattern,Email)
    if match:
        print("True to the Pattern : ", match)
    else:
        print("Match Unsucessful : ")
        Email()

def phNumber():
    phoneNum = input("Enter the phone number with country code : ")
    pattern = '\d{12}'
    match = re.match(pattern,phoneNum)
    if match:
        print("True to the Pattern : ", match)
    else:
        print("Match Unsucessful : ")
        phNumber()

def password():
    phoneNum = getpass.getpass("Enter the desired password : ")
    pattern = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    match = re.match(pattern,phoneNum)
    if match:
        print("True to the Pattern : ", match)
    else:
        print("Match Unsucessful : ")
        password()


def main():
    
    fName()
    lName()
    eMail()
    phNumber()
    password()


if __name__ == "__main__":
    main()