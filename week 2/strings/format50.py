"""
Title - Write a Python program to display formatted text (width=50) as output.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 

import textwrap



txt1 = '''
If you are having a weird bootloop where the phone just reboots after few seconds of booting like shown here (https://www.youtube.com/watch?v=3YcWsWYQVGQ) then you're in the right place, here's how you can fix the issue.
Before proceeding make sure you know your risks as I am not responsible for bricked devices, dead SD cards, thermonuclear war and anything really.
Steps:
1) Download Mi Flash Tool and install it. (For the drivers, skip it if you have installed the drivers already)
2) Download and Install minimal ADB and Fastboot Tool, persist.img and temporary twrp.img links will be below.
3) Copy the persist.img to your internal storage.
'''
print()
print(textwrap.fill(txt1, width=50))
print()
