"""
Title - Write a Python program to remove an item from a tuple.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 

tu = tuple(input("Enter the values of tuple : "))
print(tu)
# To remove an item from tuple: 
li = list(tu)
rem = input("Enter the value you want to remove : ")
for items in li:
    if items == rem:
       li.remove(rem)

tu = tuple(li)
print(tu)



