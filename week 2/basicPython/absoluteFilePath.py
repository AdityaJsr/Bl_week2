"""
Title - Write a Python program to get an absolute file path.
Author name - Aditya Kumar
Ceation time - ‎‎02 ‎March ‎2021 ‏‎
Modified time - ‎‎‎02 ‎March ‎2021‎

"""


import os

def absolute_file_path(path_fname):
    return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("listNtuple.py"))

#returns the absolute path