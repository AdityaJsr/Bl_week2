"""
 Write a Python program to print the calendar of a given month and year.

"""

import calendar

try:
    year = int(input("Enter the year : "))
    month = int(input("Enter the month : "))
except Exception as e:
    print("Oops something went wrong!!!")

print(calendar.month(year,month))