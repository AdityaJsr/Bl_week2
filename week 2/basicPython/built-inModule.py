'''
Write a Python program to find the available built-in modules

'''

import sys
import textwrap

def sysModule():
    module_name = ', '.join(sorted(sys.builtin_module_names))
    print(textwrap.fill(module_name, width=70))

if __name__ =="__main__":
    sysModule()