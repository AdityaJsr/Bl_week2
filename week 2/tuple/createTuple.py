"""
Title - Write a Python program to create a tuple.
Author name - Aditya Kumar
Ceation time - ‎‎05 ‎March ‎2021 ‏‎
Modified time - ‎‎‎05 ‎March ‎2021‎

""" 


def user_input():
    a = input("Enter the values for the tuple with a space : ").split(' ')
    tup = (tuple(a)) 
    print(tup, type(tup))

if __name__ == "__main__":
    user_input()

