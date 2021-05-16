"""
Title - Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
        Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        Expected Output : ['Green', 'White', 'Black']

Author name - Aditya Kumar
Ceation time - ‎‎05 ‎March ‎2021 ‏‎
Modified time - ‎‎‎05 ‎March ‎2021‎

""" 
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
index = set([0,5,4])
for i in sorted(index,reverse= True):
    del color [i]
print(color)


                    # or


# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)


