# Write a Python program to concatenate all elements in a list into a string and return it.




def user_input():
    userInput = list(input("Enter the list you want to concatinate : ").split(','))

    return(userInput)


def converStr():
    output = ''
    userInput = user_input()
    for items in userInput:
        output += str(items)+ ' '
    print(output)

if __name__ == '__main__':
    converStr()

# listItems = ['Hello', 'Rahul', "what's" , 'up'] 
# output = ''
# for items in listItems:
#     output += str(items)+ ' '

# print(output)