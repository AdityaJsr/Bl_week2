"""
Title -  Write a Python program to sum all the items in a list
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

""" 
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8,112,-84]))
