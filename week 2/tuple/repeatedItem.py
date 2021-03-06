"""
Title - Write a Python program to find the repeated items of a tuple.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 
#create a tuple
tu = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
print(tu)
print(type(tu))
#return the number of times it appears in the tuple.
count = tu.count(4)
print("The total count of '4' is : ",count)

