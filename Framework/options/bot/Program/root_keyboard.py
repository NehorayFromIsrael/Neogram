from Program.Send import Send as Send
from Program.Button import Button as Button

def Func(Bot_Variables):



    Message = Bot_Variables[4]

    User_Privileges = Bot_Variables[8]

    if User_Privileges == "root":

        if  Message == "root":
            Send.Keyboard(Bot_Variables, "root",
                      Button.Markup("Users"),
                      Button.Markup("Add Privileges"))


