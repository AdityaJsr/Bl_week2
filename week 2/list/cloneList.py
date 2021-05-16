"""
Title - Write a Python program to clone or copy a list.
Author name - Aditya Kumar
Ceation time - ‎‎05 ‎March ‎2021 ‏‎
Modified time - ‎‎‎05 ‎March ‎2021‎

""" 
a = ['hello', 'world', 'This', 'is', 'the', 'orignal']
b = list.copy(a)
print(b)
b.remove(a[-1])
print(b)
b.append('dupliacate')
print("List 1 : ",a)
print("List 2 : ",b)