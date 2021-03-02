"""
Title - Write a Python program to print the calendar of a given month and year.
Author name - Aditya Kumar
Creation time - ‎‎02 ‎March ‎2021
Modified time - ‎‎‎02 ‎March ‎2021‏‎

"""

import calendar

try:
    year = int(input("Enter the year : "))
    month = int(input("Enter the month : "))
except Exception as e:
    print("Oops something went wrong!!!")

print(calendar.month(year,month))