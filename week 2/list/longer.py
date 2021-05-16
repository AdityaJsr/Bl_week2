"""
Title -  Write a Python program to find the list of words that are longer than n from a given list of words.
Author name - Aditya Kumar
Ceation time - ‎‎05 ‎March ‎2021 ‏‎
Modified time - ‎‎‎05 ‎March ‎2021‎

""" 
def word(n, str):
    w_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            w_len.append(x)
    return w_len	
print(word(3, "The quick brown fox jumps over the lazy dog"))




