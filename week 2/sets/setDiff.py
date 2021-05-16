"""
Title - Write a Python program to create set difference.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = setx & sety
print(setz)
# Set difference
setb = setx - setz
print(setb)
            # or
# setc = setx.difference(sety)
# print(setc)

