"""
Title - Write a Python program that accepts a comma separated sequence of words as input
        and prints the unique words in sorted form (alphanumerically).
        Sample Words : red, white, black, red, green, black
        Expected Result : black, green, red, white,red.
Author name - Aditya Kumar
Ceation time - ‎‎06 ‎March ‎2021 ‏‎
Modified time - ‎‎‎06 ‎March ‎2021‎

""" 
def sortedAlphaNum():
    userinput = input("Enter the string with comma seperated value : ").split(',')
    userinput.sort()
    userinput = set(userinput)
    print(userinput)

if __name__ == "__main__":
    sortedAlphaNum()