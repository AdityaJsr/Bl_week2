"""
Title - Write a Python program to multiplies all the items in a list.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

""" 

def mul_list(items):
    m = 1
    for x in items:
        m *= x
    return m
print(mul_list([1,2,-8,-15]))

