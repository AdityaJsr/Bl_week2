"""
Title - Write a Python program to count the number of characters (character frequency) in a string.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 
# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))


# Python3 code to demonstrate 
# each occurrence frequency using 
# collections.Counter() 
from collections import Counter 

# initializing string 
str1 = "ookla"

# using collections.Counter() to get 
# count of each element in string 
res = Counter(str1) 

# printing result 
print ("Count of all characters in the string is :\n "
										+ str(res)) 


