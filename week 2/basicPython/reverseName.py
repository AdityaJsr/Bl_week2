def user_input():
    try:
        name = input("Enter your name to reverse : ")
    except Exception as e:
        print("Oops wrong input try again : ")
        user_input()
    return name

def reverse():
    data = user_input()
    print(data[::-1]) 

if __name__ == "__main__":
    reverse()