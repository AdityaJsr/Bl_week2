"""
Title -  Write a Python program to convert a list into a nested dictionary of keys.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

list1 = [1,'meow', 2, 3,'said','the', 4,'cat']
d = current = {}
for itesms in list1:
    current[itesms] = {}
    current = current[itesms]
print(d)

