"""
Title -  Write a Python program to count the number of strings where the string length
            is 2 or more and the first and last character are same from a given list of strings.
            Sample List : ['abc', 'xyz', 'aba', '1221']
            Expected Result : 2
Author name - Aditya Kumar
Ceation time - ‎‎05 ‎March ‎2021 ‏‎
Modified time - ‎‎‎05 ‎March ‎2021‎

""" 

def match_words(words):
  counter = 0

  for word in words:
    if (len(word) > 1)and(word[0] == word[-1]):
      counter += 1
  return counter

print("The number of items that satisfy all the conditions are : ",match_words(['abc', 'xyz', 'aba', '1221']))
