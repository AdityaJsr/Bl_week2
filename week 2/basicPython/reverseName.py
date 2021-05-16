"""
Title - Write a Python program to display the entered string in reverse manner.
Author name - Aditya Kumar
Ceation time - ‎‎02 ‎March ‎2021 ‏‎
Modified time - ‎‎‎02 ‎March ‎2021‎

"""

def user_input():
    try:
        name = input("Enter your name to reverse : ")
    except Exception as e:
        print("Oops wrong input try again : ")
        user_input()
    return name

def reverse():
    data = user_input()
    print(data[::-1]) 

if __name__ == "__main__":
    reverse()