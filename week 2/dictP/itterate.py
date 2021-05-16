"""
Title - Write a Python program to iterate over dictionaries using for loops.
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""

d1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 'state': 'Jharkhand', 'name': 'rohit' }

def iterate():
    for keys,values in d1.items():
        print(keys, 'belongs to -> ' ,d1[keys])

if __name__ == "__main__":
    iterate()