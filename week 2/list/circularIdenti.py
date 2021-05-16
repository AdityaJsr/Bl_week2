"""
Title - Write a python program to check whether two lists are circularly identical.
Author name - Aditya Kumar
Ceation time - ‎‎05 ‎March ‎2021 ‏‎
Modified time - ‎‎‎05 ‎March ‎2021‎

""" 

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

