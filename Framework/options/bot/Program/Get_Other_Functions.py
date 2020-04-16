#!/usr/bin/python
import importlib
import os
import pathlib

def Func(Other_Functions_Name, *args):


    My_PATH = str(pathlib.Path().absolute())

    Folder_PATH = "\\Other_Functions"

    # - get all modules inside "Other_Functions" folder - #

    Functions_list = os.listdir(My_PATH + Folder_PATH)

    # - run bot Other_Functions - #
    for i in range(len(Functions_list)):

        if Other_Functions_Name == Functions_list[i][:-3]:
            try:


                return importlib.import_module("Other_Functions." + Functions_list[i][:-3]).Func(args)

            except:
                pass





Func("Other_Facntions_Random_Text_Example")