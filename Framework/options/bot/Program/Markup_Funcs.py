#!/usr/bin/python
import importlib
import os
import pathlib
import sys
import re

def Func(Bot_Variables):

    Message = Bot_Variables[4]


    Update = Bot_Variables[12]
    Context = Bot_Variables[14]

    My_PATH = str(pathlib.Path().absolute())


    if re.search("^win",sys.platform):
        Folder_PATH = "\\Message_Handler"
    else:
        Folder_PATH = "//Message_Handler"
    
    # - get all modules inside "Message_Handler" folder - #

    Functions_list = os.listdir(My_PATH + Folder_PATH)


    in_put = []

    for x in range(len(Functions_list)):

        in_put.append([])
        word =Functions_list[x][:-3]
        word_len = len(word)
        l = ''
        for y in range(word_len):


            if word[y] != "#":
                l = l + word[y]

                if y == word_len-1:
                    in_put[x].append(l)

            else :
                if len(l) != 0:
                    in_put[x].append(l)
                    l = ''










    # - run bot markup functions - #
    for i in range(len(Functions_list)):

        func_name = Functions_list[i][:-3]
        words = in_put[i]
        words_len = len(words)

        for z in range(words_len):
            if Message == words[z]:

                try:
                    importlib.import_module("Message_Handler." + func_name).Func(Update,Context)
                except:
                    pass





