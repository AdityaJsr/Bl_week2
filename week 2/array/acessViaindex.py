"""
Title - Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
Author name - Aditya Kumar
Ceation time - ‎‎03 ‎March ‎2021 ‏‎
Modified time - ‎‎‎03 ‎March ‎2021‎

"""
import array as arr
# import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

a = arr.array('i', [])

def user_input():
    
    for i in range (5):
        try:
            x = input("Enter the "+str([i])+"th element : ")
            a.append(int(x))
        except Exception as e:
            print("Enterd value ran into an exception ")
    print(a)
    return(a)

def userPrint():

    a = user_input()
    try:
        index = int(input("Enter the index number of the value you want to print : "))
    except IndexError:
        print("The index value is out of range : ")
    print(a[index])
    


if __name__ == "__main__":
    userPrint()

    


