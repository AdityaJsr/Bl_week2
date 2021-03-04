"""
Title - Write a Python program to remove the first occurrence of a specified element from an array.
Author name - Aditya Kumar
Ceation time - ‎‎03 ‎March ‎2021 ‏‎
Modified time - ‎‎‎03 ‎March ‎2021‎

"""

from array import *
a = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(a))
print("Remove the first occurrence of 3 from the said array:")
a.remove(3)
print("New array: "+str(a))
