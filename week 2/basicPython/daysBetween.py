'''
Write a Python program to calculate number of days between two dates
'''
from datetime import date 

startDate = date(2014, 7, 2)
endDate = date(2014, 7, 11)

print('The total number of dates are ',endDate - startDate)
