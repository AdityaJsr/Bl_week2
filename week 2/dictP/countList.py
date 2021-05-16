"""
Title - Write a Python program to count number of items in a dictionary value that is a list.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""


dict1 =  {'rahul': ['s1', 's2', 's3'], 'rajiv': ['m1', 'm2'] ,'raghu': ['b1', 'b22']}
counter = sum(map(len, dict1.values()))
print("The sum of all the values of list are :",counter)
