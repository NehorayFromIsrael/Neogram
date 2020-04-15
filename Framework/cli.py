
def StartUp():
    
    print("\n\n\t---- Neogram ----")

    description= """

    Usage:

    GUI development for Telegram Bots

-----------------------------------------------------------------
    Description:

    Neogram is a simple and easy framwork for developing and building
    Graphical User Interface (GUI) for telegram bots in Python
-----------------------------------------------------------------

     Copyrights @ Nehoray Shalom (NeohorayFromIsrael Github)
     

    \t1. Create New Telegram Bot
    \t2. Create New Multibot (capible to run multiplay telegram bots)
    \t3. Create New Function Template
    \t4. Exit
    """ 



    print(description + "\n\n")



def Run(in_put,func_list,location):
  

    for i in range(len(func_list)):

        if location == func_list[i][0] and in_put == func_list[i][1]:
            func_list[i][2]()


def create_new_bot():
    global location
    global func_list
    
    location = "create_new_bot"


    print("\n\n\t---- Create New Bot ----\n")

    in_put = input("\n\tPlease type name for your bot:\t")


    print("\n\t{} Telegram bot is generated...".format(in_put))


    print("\n\t{} Generate succssfuly".format(in_put))

    location = "break"


def xit():
    global location
    location = "break"
    print("\n\n\t---- Exit ----\n")




if __name__ == "__main__":


    func_list = [["StartUp","1",create_new_bot],["StartUp","4",xit]]

    location = "StartUp"

    StartUp()
    
    
    while True:
        in_put = input("\n\tPlesae press the number acording to your action:  ")

        Run(in_put,func_list ,location)

        if location == "break":
            break





