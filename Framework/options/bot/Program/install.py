import sys
import re
import subprocess as s


#requirements for manually installation:

# 1. use pip install for this modules
#   pymongo==3.10.1
#   python-telegram-bot==12.4.2
#   telegram==0.0.1

# 2. download AND install mongoDB


def Func(req):

    requirements = ["pymongo==3.10.1","python-telegram-bot==12.4.2","telegram==0.0.1"]

    for i in range(len(req)):
        requirements.append(req[i])

    print("install requirements...\n")
    if re.search("^win",sys.platform):
        for i in range(len(requirements)):
            print("install " + requirements[i])
            s.run("pip3 install " + requirements[i])
            print(requirements[i] + " installation completed")

    else:
        for i in range(len(requirements)):
            print("install " + requirements[i])
            s.run("sudo pip3 install " + requirements[i])
            print(requirements[i] + " installation completed")
            
    print("\nrequirements installation completed")




if __name__ == "__main__":

    Func()
    
