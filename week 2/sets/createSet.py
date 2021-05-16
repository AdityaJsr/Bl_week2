"""
Title -  Write a Python program to create a set.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

def createSet():
    a = input("Enter the ',' seperated values you want in your set : ").split(',')
    print (a,'The count is : ' ,len(a))
    b = set(a)
    print(b,'The count is : ', len(b))


if __name__ == "__main__":
    createSet()