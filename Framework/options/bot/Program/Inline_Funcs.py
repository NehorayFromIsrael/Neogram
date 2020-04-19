#!/usr/bin/python
import importlib
import os
import pathlib
import re
import sys

def Func():


    List = []

    My_PATH = str(pathlib.Path().absolute())

    if re.search("^win",sys.platform):
        Folder_PATH = "\\Inline_Functions"
    else:
        Folder_PATH = "//Inline_Functions"

    # - get all modules inside "Inline_Functions" folder - #

    Functions_list = os.listdir(My_PATH + Folder_PATH)



    # - import bot inline functions and append to list- #
    for i in range(len(Functions_list)):

        try:
           f = importlib.import_module("Inline_Functions." + Functions_list[i][:-3])

           List.append([f.Func,Functions_list[i][:-3]])


        except:
            pass


    return List

if __name__ == "__main__":

    print(Func())
