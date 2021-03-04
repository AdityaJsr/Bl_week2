"""
Title - Write a Python program to create a dictionary from a string.
        Note: Track the count of the letters from the string.
        Sample string : 'w3resource'
        Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 
        Access individual element through indexes.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

from collections import defaultdict, Counter


str1 = 'thisIsaSampleString' 
d = {}
for letter in str1:
    d[letter] = d.get(letter, 0) + 1
print(d)
