from Program.Send import Send as Send
from Program.Button import Button as Button

def Func(Bot_Variables):



    Message = Bot_Variables[4]

    User_Privileges = Bot_Variables[8]

    if User_Privileges == "root":

        if  Message == "root":
            Send.Keyboard(Bot_Variables, "root",
                      Button.Markup("Assets","Users"),
                      Button.Markup("Add Privileges"),
                      Button.Markup(Button.Markup_Phone("update chat id in assets via phone")))

