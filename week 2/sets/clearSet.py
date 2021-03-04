"""
Title -  Write a Python program to clear a set
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

""" 
 
setp = set(["rahul", "ranger","@football"])
setq = setp.copy() # copying the orignal into an empty set
print(setq)
setq.clear()        # The clear function
print(setq)         # Empty set after being cleared
