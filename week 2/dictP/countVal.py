"""
Title -  Write a Python program to count the values associated with key in a dictionary.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

stu = [{'id': 1, 'success': True, 'name': 'Lary', 'grade': 45 },
 {'id': 2, 'success': False, 'name': 'Rabi', 'grade': 15},
 {'id': 3, 'success': True, 'name': 'Alex', 'grade': 50}]

print(sum(d['id'] for d in stu))

print(sum(d['grade'] for d in stu))
