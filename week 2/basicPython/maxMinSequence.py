"""
Title - Write a Python function to find the maximum and minimum numbers from a sequence of
numbers
on operating system.
Author name - Aditya Kumar
Ceation time - ‎‎03 ‎March ‎2021 ‏‎
Modified time - ‎‎‎03 ‎March ‎2021‎

"""
def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

# print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
