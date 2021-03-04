"""
Title -  Write a Python program to add member(s) in a set.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

color_set = set()
color_set.add("Red")
print(color_set)
#Update multiple items
color_set.update(["Blue", "Green"])
print(color_set)
a = input("Enter the color you want to ad to the set : ")
color_set.add(a)
print(color_set)
b = list(input("Enter the color you want to update to the set : ").split(','))
color_set.update(b)
print(color_set)
