import os.path, time

def createmodifyTime():
    print("Last modified: %s" % time.ctime(os.path.getmtime("numOfCpu.py")))
    print("Created: %s" % time.ctime(os.path.getctime("numOfCpu.py")))

if __name__ == "__main__":
    createmodifyTime()