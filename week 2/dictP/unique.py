"""
Title - Write a Python program to print all unique values in a dictionary.
        Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""
a =set()
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
# for dic in L:
#     for val in dic.values():
#         u = set(val)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)


# for dic in L:
#     for val in dic.values():
#         a.update(set(val))
# print (a)