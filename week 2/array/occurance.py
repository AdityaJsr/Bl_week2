"""
Title - Write a Python program to get the number of occurrences of a specified element in an array.
Access individual element through indexes.
Author name - Aditya Kumar
Ceation time - ‎‎03 ‎March ‎2021 ‏‎
Modified time - ‎‎‎03 ‎March ‎2021‎

"""

from array import *



array_num = array('i', [1, 3, 5, 3, 7, 9, 1])
print("Original array: "+str(array_num))

print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))



## Actual Working of Count :

# print(" ")
# print("Counting Ocuurence using loop")
# x = [1, 3, 5, 3, 7, 9, 1]
# count = 0

# for i in range(len(x)):
#     if x[i] == 3:
#         count = count + 1

# print("Occurences of 3 :" + str(count))
