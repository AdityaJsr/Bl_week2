"""
Title - Write a Python program to sort files by date.
Author name - Aditya Kumar
Ceation time - ‎‎03 ‎March ‎2021 ‏‎
Modified time - ‎‎‎03 ‎March ‎2021‎

"""

import glob
import os

files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))
