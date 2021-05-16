"""
Title - Write a Python program to create a union of sets..
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

# Union of sets
setx = set(["physics", "chemistry","biology","history"])
sety = set(["math", "chemistry","hindi","english","history"])
# setz = setx.union(sety)
# or    
seta = setx | sety
print(seta)

