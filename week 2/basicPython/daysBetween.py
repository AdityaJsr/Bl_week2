"""
Title - Write a Python program to calculate number of days between two dates.
Author name - Aditya Kumar
Ceation time - ‎‎02 ‎March ‎2021 ‏‎
Modified time - ‎‎‎02 ‎March ‎2021‎

"""

from datetime import date 

startDate = date(2014, 7, 2)
endDate = date(2014, 7, 11)

print('The total number of dates are ',endDate - startDate)
