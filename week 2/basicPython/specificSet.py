'''
Write a Python program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
'''

setA = set(["White", "Black", "Red"])
setB = set(["Red", "Green"])

setC = setA.difference(setB)
print(setC)