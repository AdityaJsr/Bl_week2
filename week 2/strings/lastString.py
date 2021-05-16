"""
Title - Write a Python program to get the last part of a string before a specified character.
        https://www.w3resource.com/python-exercises
        https://www.w3resource.com/python
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])


