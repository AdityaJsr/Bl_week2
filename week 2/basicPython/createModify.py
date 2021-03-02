import os.path, time

def createmodifyTime():
    print("Last modified: %s" % time.ctime(os.path.getmtime("numOfCpu.py")))
    print("Created: %s" % time.ctime(os.path.getctime("numOfCpu.py")))

    print("Last modified: %s" % time.ctime(os.path.getmtime("D:\music\Music\[Songs.PK] 02 - Heropanti - Rabba.mp3")))
    print("Created: %s" % time.ctime(os.path.getctime("D:\music\Music\[Songs.PK] 02 - Heropanti - Rabba.mp3")))
if __name__ == "__main__":
    createmodifyTime()