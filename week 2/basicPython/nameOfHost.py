'''
Write a Python program to get the name of the host on which the routine is running.

'''



import socket

def getSocketName():
    host_name = socket.gethostname()
    print("Host name:", host_name)

if __name__ == '__main__':
    getSocketName()