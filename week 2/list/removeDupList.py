"""
Title - Write a Python program to remove duplicates from a list of lists.
        Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        New List : [[10, 20], [30, 56, 25], [33], [40]]
Author name - Aditya Kumar
Ceation time - ‎‎05 ‎March ‎2021 ‏‎
Modified time - ‎‎‎05 ‎March ‎2021‎

""" 

import itertools

num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", num)
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)


