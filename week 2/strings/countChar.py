"""
Title - Write a Python program to count the number of characters (character frequency) in a string.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 
from collections import Counter 

def method1 ():   
    def char_frequency(str1):
        dict = {}
        for n in str1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        return dict
    print(char_frequency('pneumonoultramicroscopicsilicovolcanoconiosis'))


def method2():
    # initializing string 
    str1 = "ookla"

    # using collections.Counter() to get 
    # count of each element in string 
    res = Counter(str1) 

    # printing result 
    print ("Count of all characters in the string is :\n "
                                            + str(res)) 


if __name__ == "__main__":
    try:
        ch = int(input("Enter 1 or 2 to select the desied method : "))
    except Exception as e:
        print("There seems to be an exception", e)
    if ch == 1:
        method1()
    elif(ch == 2):
        method2()
    else:
        print("Choice Error : ")