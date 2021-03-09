'''
Title - User Registration System matches user's First, last name EmailID,
        phoneNum, Password. with regEx pattern.
Author name - Aditya Kumar
Ceation time - ‎‎08 ‎March ‎2021 ‏‎
Modified time - ‎‎‎08 ‎March ‎2021‎

'''


import re

def fName():
    FirstName = input("Enter the First name : ")
    pattern = '(^[A-Z][a-zA-Z]{2,})'
    match = re.match(pattern,FirstName)
    if match:
        print("True to the Pattern : ", match)
    else:
        print("Match Unsucessful : ")
        fName()



def main():
    
    fName()



if __name__ == "__main__":
    main()