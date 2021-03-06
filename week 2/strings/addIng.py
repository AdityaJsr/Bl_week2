"""
Title -  Write a Python program to add 'ing' at the end of a given string (length should be atleast 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
        given string is less than 3, leave it unchanged.
        Sample String : 'abc'
        Expected Result : 'abcing'
        Sample String : 'string'
        Expected Result : 'stringly
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
