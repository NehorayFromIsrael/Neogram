import sys
import pathlib
from distutils.dir_util import copy_tree
from shutil import copyfile
import shutil
import os
import re

def check_if_file_exist(file_name):
    My_PATH = str(pathlib.Path().absolute())

    list = os.listdir(My_PATH)

    check = True
    for i in range(len(list)):
        if file_name == list[i]:
            check = False
    return check


def StartUp():

    Neogram = """
  _   _                                       
 | \ | |                                      
 |  \| | ___  ___   __ _ _ __ __ _ _ __ ___   
 | . ` |/ _ \/ _ \ / _` | '__/ _` | '_ ` _ \  
 | |\  |  __/ (_) | (_| | | | (_| | | | | | | 
 |_| \_|\___|\___/ \__, |_|  \__,_|_| |_| |_| 
                    __/ |                     
                   |___/                                     
    """

    Neogram = """
            ███╗   ██╗███████╗ ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    
            ████╗  ██║██╔════╝██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    
            ██╔██╗ ██║█████╗  ██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║    
            ██║╚██╗██║██╔══╝  ██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║    
            ██║ ╚████║███████╗╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║    
            ╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    
    """
    print( Neogram)

    description= """
    Usage:

    GUI development for Telegram Bots

-----------------------------------------------------------------
    Description:

    Neogram is a simple and easy framework for developing and building
    Graphical User Interface (GUI) for telegram bots in Python
-----------------------------------------------------------------

     Copyrights @ Nehoray Shalom (NeohorayFromIsrael Github) Email: neosh8132@gmail.com
     
    \t1. Create New Telegram Bot
    \t2. Create New Multibot (capible to run multiplay telegram bots)
    \t3. Create New Function Template
    \t4. Help
    \t5. Exit
    """ 



    print(description )



def Run(in_put,func_list,location):
  

    for i in range(len(func_list)):

        if location == func_list[i][0] and in_put == func_list[i][1]:
            func_list[i][2]()


def create_new_bot(in_put=None):
    global location
    global func_list
    global linux_path
    location = "create_new_bot"


    print("\n\n\t---- Create New Bot ----\n")


    if in_put == None:
        while True:
            in_put = input("\n\tPlease type name for your bot:\t")
            if not check_if_file_exist(in_put):
                print("\n\tSorry file name already exist in current path")
            else: break

    print("\n\t{} Telegram bot is generated...".format(in_put))

    if not check_if_file_exist(in_put):
        print("\n\tSorry file name already exist in current path")
    else:

        if re.search("^win", sys.platform):
            copy_tree("C:\\Program Files\\Neogram\\options\\bot", str(pathlib.Path().absolute()) +"\\" +in_put)
        else: copy_tree(linux_path + "//Neogram//options//bot", str(pathlib.Path().absolute()) +"//" +in_put)
        print("\n\t{} Generated successfully".format(in_put))

    location = "break"


def xit():
    global location
    location = "break"
    print("\n\n\t---- Exit ----\n")


def create_new_template(in_put=None,type=None):
    global location
    global linux_path

    location = "create_new_template"


    print("\n\n\t---- Create New Template ----\n")

    if type == None:

        print("\n\t1. Message Handler")
        print("\n\t2. Inline Functions")

        type = input("\n\tWhat template do you need?, For Message Handler OR Inline Functions ?\t")

    if in_put == None:
        while True:
            in_put = input("\n\tPlease type name for your Function:\t")


            if not check_if_file_exist(in_put+".py") == True:
                print("\n\tSorry file name already exist in current path")
            else:
                break

    if check_if_file_exist(in_put+".py") == True:

        if type == "1" or type == "-M":
            if re.search("^win", sys.platform):
                shutil.copy2("C:\\Program Files\\Neogram\\options\\templates\\Message_Handler_Template.py", str(pathlib.Path().absolute()) +"\\" +in_put + ".py")
            else:
                shutil.copy2(linux_path + "//Neogram//options//templates//Message_Handler_Template.py", str(pathlib.Path().absolute()) +"//" +in_put + ".py")

        if type == "2" or type == "-I":
            if re.search("^win", sys.platform):
                shutil.copy2("C:\\Program Files\\Neogram\\options\\templates\\Inline_Functions_Template.py", str(pathlib.Path().absolute()) +"\\" +in_put + ".py")
            else:
                shutil.copy2(linux_path + "//Neogram//options//templates//Inline_Functions_Template.py", str(pathlib.Path().absolute()) +"//" +in_put + ".py")

        print("\n\t{} Generated successfully".format(in_put))

    else:
        print("\n\tSorry file name already exist in current path")

    location = "break"



def create_new_multibot(in_put=None):
    global location

    location = "create_new_multibot"

    print("\n\n\t---- Create New Multibot ----\n")

    if in_put == None:
        while True:
            in_put = input("\n\tPlease type name for your multibot:\t")
            if not check_if_file_exist(in_put):
                print("\n\tSorry file name already exist in current path")
            else:
                break

    print("\n\t{} Telegram multibot is generated...".format(in_put))

    if not check_if_file_exist(in_put):
        print("\n\tSorry file name already exist in current path")
    else:
        if re.search("^win", sys.platform):
            copy_tree("C:\\Program Files\\Neogram\\options\\multibot", str(pathlib.Path().absolute()) + "\\" + in_put)
        else:
            copy_tree(linux_path + "//Neogram//options//multibot", str(pathlib.Path().absolute()) + "//" + in_put)

        print("\n\t{} Generated successfully".format(in_put))

    location = "break"


def help():
    print("help")



if __name__ == "__main__":

    linux_path = ""
    check_if_file_exist(file_name="g")
    argv_len = len(sys.argv)

    if argv_len  == 1:
        func_list = [["StartUp","1",create_new_bot],["StartUp","5",xit],["StartUp","3",create_new_template],["StartUp","2",create_new_multibot],["StartUp","4",help]]

        location = "StartUp"

        StartUp()
    
    
        while True:
            in_put = input("\n\tPlease type the number according to your action:  ")

            Run(in_put,func_list ,location)

            if location == "break":
                break

    elif argv_len >= 2:

        if sys.argv[1] == "new-bot":
            try: create_new_bot(in_put=sys.argv[2])
            except : create_new_bot()

        if sys.argv[1] == "new-multibot":
            try: create_new_multibot(in_put=sys.argv[2])
            except : create_new_multibot()

        if sys.argv[1] == "new-t":
            try: create_new_template(in_put=sys.argv[3], type=sys.argv[2])
            except: create_new_template()

        if sys.argv[1] == "-h":
            help()


