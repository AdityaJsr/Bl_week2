"""
Title -  Write a Python program to add 'ing' at the end of a given string (length should be atleast 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
        given string is less than 3, leave it unchanged.
        Sample String : 'abc'
        Expected Result : 'abcing'
        Sample String : 'string'
        Expected Result : 'stringly
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 
# Enter the else statement

def add_string():
    str1 = input("Enter the input string : ")
    len1 = len(str1)
    if len1 > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    else:
        print("The minimum characters are not present : ",len(str1))
        add_string()
    
    print(str1)

if __name__ == "__main__":
    add_string()





