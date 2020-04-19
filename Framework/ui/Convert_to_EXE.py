import subprocess as s
import ctypes, os
from distutils.dir_util import copy_tree
import shutil



def run_Func():


    requirements = ["PyInstaller==3.6"]

    print("install " + requirements[0])
    s.run("pip3 install " + requirements[0])
    print(requirements[0] + " installation completed")

    print("\n\ncompile exe file by pyinstaller...")
    s.run("pyinstaller Framework\\ui\\Neogram.py")
    print("compiled exe successfully")

    print("\n\ntransering files...")
    s.run("Xcopy /E /I /y Framework\\options dist\\Neogram\\options")

    copy_tree("dist", "C:\\Program Files")

    shutil.rmtree("build")

    os.remove("Neogram.spec")
    shutil.rmtree("dist")


    print("transferred successfully")

    print("\n\nadding path")
    s.run('setx path "%path%;C:\\Program Files\\Neogram"')

    print("\n\npath added successfully")

    print("\n\n-------- instalation completed, Restart CMD and type 'Neogram' command to lunch neogram --------")

    



def Func():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
         is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0


    if is_admin == True:
        run_Func()
    else:

        print("you not runing this file as as Administrator, Please run with Administrator privileges ")

















        
