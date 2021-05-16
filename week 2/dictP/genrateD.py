"""
Title - Write a Python script to generate and print a dictionary that contains a
        number (between 1 and n) in the form (x, x*x).
        Sample Dictionary ( n = 5) :
        Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Author name - Aditya Kumar
Ceation time - ‎‎04 ‎March ‎2021 ‏‎
Modified time - ‎‎‎04 ‎March ‎2021‎

"""
d = dict()

def user_input():
    num=int(input("Input the number you want to create the Key:Value pair of : "))
    return (num)

def genrateD():
    num  = user_input()

    for item in range(1,num+1):
        d[item]=item*item
    print(d) 

if __name__ == "__main__":
    genrateD()