"""
title - This is the test case for the user registration RegEx.
author name - Aditya Kumar
creation time - 9 march 2021
modified time - 9 march ‎2021
"""


import unittest
from userRegex import *

class userRegex(unittest.TestCase):


    def test_first_Name(self):
        result = (first_Name('Aditya'))
        self.assertEqual(result,True)
        result = (first_Name('aditya'))
        self.assertEqual(result,False)
        result = (first_Name('123Aditya'))
        self.assertEqual(result,False)
        result = (first_Name('Rohit'))
        self.assertEqual(result,True)
        result = (first_Name('adi'))
        self.assertEqual(result,False)
        result = (first_Name('Adi'))
        self.assertEqual(result,True)

    def test_last_Name(self):
        result = (last_Name('Kumar'))
        self.assertEqual(result,True)
        result = (last_Name('kumar'))
        self.assertEqual(result,False)
        result = (last_Name('123Kumar'))
        self.assertEqual(result,False)
        result = (last_Name('Das'))
        self.assertEqual(result,True)
        result = (last_Name('Ku'))
        self.assertEqual(result,False)
        result = (last_Name('Da'))
        self.assertEqual(result,False)

    def test_emailValid(self):
        result = (emailValid('adityajsr199@gmail.com'))
        self.assertEqual(result,True)
        result = (emailValid('aditya@123'))
        self.assertEqual(result,False)
        result = (emailValid('adityjsr@gmail.comin'))
        self.assertEqual(result,False)
        result = (emailValid('abcd.121@linkedin.in'))
        self.assertEqual(result,True)
        result = (emailValid('1@gmail.com'))
        self.assertEqual(result,False)
        result = (emailValid('aditya123@123.in'))
        self.assertEqual(result,False)

    def test_phonenum_validate(self):
        result = (phonenum_validate('91 7277727650'))
        self.assertEqual(result,True)
        result = (phonenum_validate('917277727650'))
        self.assertEqual(result,False)
        result = (phonenum_validate('7277727650'))
        self.assertEqual(result,False)
        result = (phonenum_validate('84 7277727642'))
        self.assertEqual(result,True)
        result = (phonenum_validate('4852595962'))
        self.assertEqual(result,False)
        result = (phonenum_validate('78894556122349'))
        self.assertEqual(result,False)

    def test_validate_password(self):
        result = (validate_password('Aditya@123'))
        self.assertEqual(result,True)
        result = (validate_password('aditya@123'))
        self.assertEqual(result,False)
        result = (validate_password('aditya123'))
        self.assertEqual(result,False)
        result = (validate_password('Adity1@2bc'))
        self.assertEqual(result,True)
        result = (validate_password('ad@123'))
        self.assertEqual(result,False)
        result = (validate_password(' '))
        self.assertEqual(result,False)

if __name__ == '__main__':
    unittest.main()