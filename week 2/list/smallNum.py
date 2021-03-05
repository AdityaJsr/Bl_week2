"""
Title -  Write a Python program to get the smallest number from a list.
Author name - Aditya Kumar
Ceation time - ‎‎05 ‎March ‎2021 ‏‎
Modified time - ‎‎‎05 ‎March ‎2021‎

""" 

def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print("The smallest number in the list is : ",smallest_num_in_list([1, 2, -8, 0]))

#            or
# # list of numbers
# list1 = [10, 20, 4, 45, 99, -99, -2]
 
# # sorting the list
# list1.sort()
 
# # printing the first element
# print("Smallest element is:", *list1[:1])