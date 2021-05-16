"""
Title -  Write a Python program to remove item(s) from set
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

color_set = set()
color_set.add("Red")
print(color_set)
#Update multiple items
color_set.update(["Blue", "Green","Cyan","Amber"])
print(color_set)
try:
    a = input("Enter the color you want to remove to the set : ")
    color_set.remove(a)
except ValueError as v:
    print("value not found : ", v)
except Exception as e:
    print("Oops something went wrong!!", e)

print(color_set)

