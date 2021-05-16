"""
Title - Write a Python to display the given string in list and tuple.
Author name - Aditya Kumar
Ceation time - ‎‎02 ‎March ‎2021 ‏‎
Modified time - ‎‎‎02 ‎March ‎2021‎

"""

def user_input():
    try:
        userInput = input("Enter the comma sperated number here : ").split(',')
    except Exception as e:
        print("Oops wrong input try again : ")
        user_input()
    return(userInput)

def sliceNdice():
    data = user_input()
    a = []
    a = data
    b = tuple(data)
    print(a, type(a))
    print(b,type(b))

if __name__ == "__main__":
    sliceNdice()