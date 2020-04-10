#!/usr/bin/python
import importlib
import os
import pathlib

def Func(Bot_Variables,Content_Name):


    My_PATH = str(pathlib.Path().absolute())

    Folder_PATH = "\\Content"

    # - get all modules inside "Content" folder - #

    Functions_list = os.listdir(My_PATH + Folder_PATH)


    # - run bot Content functions - #
    for i in range(len(Functions_list)):

        if Content_Name == Functions_list[i][:-3]:
            try:
                importlib.import_module("Content." + Functions_list[i][:-3]).Func(Bot_Variables)


            except:
                pass





