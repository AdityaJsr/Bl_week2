"""
Write a Python program to check whether a specified value is contained in a group of values

"""

def user_input():
    userInput = list(input("Enter the main list : ").split(','))
    key = input("Enter the value you want to search : ")
    my_set = set(userInput)
    return(my_set,key)

def search():
    my_set,key = user_input()
    print(my_set,key)
    if key in my_set:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    search()

