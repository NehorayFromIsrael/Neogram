#!/usr/bin/python
import importlib
import os
import pathlib

def Func(Bot_Variables):

    Message = Bot_Variables[4]

    Update = Bot_Variables[12]
    Context = Bot_Variables[14]

    My_PATH = str(pathlib.Path().absolute())

    Folder_PATH = "\\Message_Handler"

    # - get all modules inside "Message_Handler" folder - #

    Functions_list = os.listdir(My_PATH + Folder_PATH)


    # - run bot markup functions - #
    for i in range(len(Functions_list)):

        if Message == Functions_list[i][:-3]:
            try:
             importlib.import_module("Message_Handler." + Functions_list[i][:-3]).Func(Update,Context)


            except:
                 pass





