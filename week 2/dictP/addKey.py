"""
Title - Write a Python script to add a key to a dictionary.
        Sample Dictionary : {0: 10, 1: 20}
        Expected Result : {0: 10, 1: 20, 2: 30} 
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""
d = {0: 10, 1: 20}
print (d)

def user_input():
    try:
        a = int(input("Enter the key : "))
        b = int(input("Enter the value : "))
        d.update({a:b})
    except Exception as e:
        print("Ran into an error", e)
    print (d)

if __name__ == "__main__":
    user_input()