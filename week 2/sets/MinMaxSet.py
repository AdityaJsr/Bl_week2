"""
Title -  Write a Python program to find maximum and the minimum value in a set.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

""" 

#Create a set
set1 = set([5, 10, 3, 15, 2, 20])
#Find maximum value
print(max(set1))
#Find minimum value
print(min(set1))
a = int(input("Enter the value you want to append : "))
set1.add(a)
#Find maximum value
print(max(set1))
#Find minimum value
print(min(set1))
