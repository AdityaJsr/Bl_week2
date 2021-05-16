'''
Title - User Registration System matches user's First, last name EmailID,
        phoneNum, Password. with regEx pattern.
Author name - Aditya Kumar
Ceation time - ‎‎08 ‎March ‎2021 ‏‎
Modified time - ‎‎‎09 ‎March ‎2021‎

'''


import re
import getpass



def firstNameInput():
    try:
        FirstName = input("Enter the First name : ")
    except Exception as e:
        print("Ran into an exception : ", e)
    if not first_Name(FirstName):
        firstNameInput()

def first_Name(FirstName):
    pattern = '(^[A-Z][a-zA-Z]{2,})'
    match = re.match(pattern,FirstName)
    if match:
        print("True to the Pattern : ", match)
        return True
    else:
        print("Match Unsucessful : ")
        return False
        
        

def lastNameInput():
    try:
        LastName = input("Enter the Last name : ")
    except Exception as e:
        print("Ran into an exception : ", e)
    if not last_Name(LastName):
        lastNameInput()

def last_Name(LastName):
    pattern = '(^[A-Z][a-zA-Z]{2,})'
    match = re.match(pattern,LastName)
    if match:
        print("True to the Pattern : ", match)
        return True
    else:
        print("Match Unsucessful : ")
        return False
        
def userEmailInput():
    try:
        Email = input("Enter your Email Id : ")
    except Exception as e:
        print("Ran into an exception : ",e)
    if not emailValid(Email):
        userEmailInput()

def emailValid(Email):
    pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@][a-z]+[.]\w{2,3}$'
    match = re.match(pattern,Email)
    if match:
        print("True to the Pattern : ", match)
        return True
    else:
        print("Match Unsucessful : ")
        return False


def phoneNumInput():
    try:
        phoneNum = input("Enter the phone number with country code : ")
    except Exception as e:
        print("Ran into an exception : ",e)
    if not phonenum_validate(phoneNum):
        phoneNumInput()

def phonenum_validate(phoneNum):
    
    pattern = '\d{2} \d{10}'
    match = re.match(pattern,phoneNum)
    if match:
        print("True to the Pattern : ", match)
        return True
    else:
        print("Match Unsucessful : ")
        return False
def passwordInput():
    try:
        passWord = getpass.getpass("Enter the desired password : ")
    except Exception as e:
        print("Ran into an exception : ",e)
    if not validate_password(passWord):
        passwordInput()   

def validate_password(passWord):
    
    pattern = "^(?=.*[A-Za-z])(?=.*[A-Z])(?=.*[@$!%*#?&])[A-Za-z0-9\d@$!%*#?&]{8,}$"
    match = re.match(pattern,passWord)
    if match:
        print("True to the Pattern : ", match)
        return True
    else:
        print("Match Unsucessful : ")
        return False


def main():
    
    firstNameInput()
    lastNameInput()
    userEmailInput()
    phoneNumInput()
    passwordInput()


if __name__ == "__main__":
    main()