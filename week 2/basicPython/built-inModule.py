"""
Title - Write a Python program to find the available built-in modules.
Author name - Aditya Kumar
Creation time - ‎‎02 ‎March ‎2021
Modified time - ‎‎‎02 ‎March ‎2021‏‎

"""

import sys
import textwrap

def sysModule():
    module_name = ', '.join(sorted(sys.builtin_module_names))
    print(textwrap.fill(module_name, width=70))

if __name__ =="__main__":
    sysModule()