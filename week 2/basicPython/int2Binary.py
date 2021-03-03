"""
Title - Write a Python program to convert an integer to binary keep leading zeros.
Author name - Aditya Kumar
Ceation time - ‎‎03 ‎March ‎2021 ‏‎
Modified time - ‎‎‎03 ‎March ‎2021‎

"""



def user_input():
    a = int(input("Enter the number to get it's binary equivallent : "))
    print(format(a, '08b'))
    print(format(a, '010b'))

if __name__ == "__main__":
    user_input()