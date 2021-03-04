"""
Title -  Write a Python program to check multiple keys exists in a dict1ionary.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

dict1 = {
  'name': 'rahul',
  'class': 'XII',
  'rollNo': '15'
}
print('The value is',dict1.keys() >= {'class', 'name'})
print('The value is',dict1.keys() >= {'name', 'rahul'})
print('The value is',dict1.keys() >= {'rollNo', 'name'})
print('The value is',dict1.keys() == {'class', 'name','rollNo'})
