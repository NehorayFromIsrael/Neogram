from sys import argv 






if __name__ == "__main__":
 


    description= """

Usage:

GUI development for Telegram Bots

-----------------------------------------------------------------
Description:

Neogram is a simple and easy framwork for developing and building
Graphical User Interface (GUI) for telegram bots in Python
-----------------------------------------------------------------


To create new bot type: neogram new-bot "BotName"
""" 

    epilog="Copyrights @ Nehoray Shalom (NeohorayFromIsrael Github)"



    arg = argv



    if len(arg) == 1:
        print(description + "\n\n" + epilog)


    if len(arg) >= 2:
        
        if arg[1] == "new-bot":
            try:
                print("Generate bot " + arg[2])
            except:
                print("please give name to you bot")
