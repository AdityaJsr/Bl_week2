"""
Title - Write a Python program to reverse the order of the items in the array.
Access individual element through indexes.
Author name - Aditya Kumar
Ceation time - ‎‎03 ‎March ‎2021 ‏‎
Modified time - ‎‎‎03 ‎March ‎2021‎

"""

import array as arr



def revArray():
    a = arr.array('d',[20.5,25.8,30.9,55.6,100,201,2,98.6])
    print("\nOriginal array: "+str(a)+"\n")
    print("Reverse the order of the items:")
    a.reverse()
    print(str(a)+"\n\n")





    # l = len(a)
    # b = arr.array['d',[]]
    # for items in range (l):
    #     b.append(a[l-1])
    #     l -= 1
    # print (b)

if __name__ == "__main__":
    revArray()