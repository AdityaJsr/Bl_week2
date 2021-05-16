"""
Title - Write a Python program to remove a key from a dictionary.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""


d1 = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(d1)

def deleteVal():
    key = input("Enter the key of the value you want to delete : ")
    if key in d1:

        del d1[key]
    
    print(d1)


if __name__ == "__main__":
    deleteVal()