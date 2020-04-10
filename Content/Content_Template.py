from Program.Send import Send as Send
from Program.Button import Button as Button
import Program.Get_Other_Functions as Get_Other_Functions

# - use this template to create the content in your bot like : keyboard,inline keyboard and text messages, functions are listed down below - #
# - its highly recommended not to change any line from this template (just add your code down below, dont edit any existing lines) - #


# -In order to use Send Functions you have to import Send module: "from Program.Send import Send" - #
# -In order to use Button Functions you have to import Button module: "from Program.Button import Button as Button" - #
# -in order to use "Get_Other_Functions.Func(Other_Function_Name,*args)" you have to import this module: "import Program.Get_Other_Functions as Get_Other_Functions"

"""

Send.Message(Bot_Variables,"Paste Text Here")

Send.Keyboard(Bot_Variables, "Text Here",
                  Button.Markup("button 1"),
                  Button.Markup("button 2", "button 3"),
                  Button.Markup("button 4", "button 5", "button 6"))



#NOTE: when when you used Button.Inline() for creating buttons for inline keyboard this is the syntax:
# ["URL/CALLBACK Button type( u/c )","button text","the url or callback name"]
# the callback name is the name you gave to the file you created in "Inline_Function" folder (not include the .py extinction)

Send.Inline_Keyboard(Bot_Variables, "Text Here" ,
                         Button.Inline(  ["U","URL Button","https://www.google.co.il/"] ,  ["C","Callback Button","Template"] ) ,
                         Button.Inline(["C","Callback Button","Template"] ,["U","URL Button","https://www.google.co.il/"])
                         )

# send edited keyboard, its edit current inline keyboard and change buttons give deep navigation effect

Send.Edited_Inline_Keyboard(Bot_Variables,"Text Here",
                            Button.Inline(["u","URL Button","www.google.co.il"])
                            )


"""


    # - Variables - #
"""
    TOKEN = Bot_Variables[0]
    Chat_ID = Bot_Variables[1]
    First_Name = Bot_Variables[2]
    UserName = Bot_Variables[3]
    Message = Bot_Variables[4]
    Message_ID = Bot_Variables[5]
    File_ID = Bot_Variables[6]
    Virtual_Location = Bot_Variables[7]
    User_Privileges = Bot_Variables[8]
    User_Lang = Bot_Variables[9]
    Mongo_Collections = Bot_Variables[10]
    Json_Message = Bot_Variables[11]
    Update = Bot_Variables[12]
    Other_Variables = Bot_Variables[13]

    * in order to use : "Get_Content.Func(Bot_Variables,"Content_File_Name")" command you have to import Get_Content Module: "import Program.Get_Content as Get_Content"
    #  USE "Get_Content.Func(Bot_Variables,"Content_File_Name")" to send the Desire Content like keyboards,inline keyboards and text messages you created in "Content" folder
    # Try this Example:

    # Get_Content.Func(Bot_Variables,"Content_Message_Text_Example")
    # Get_Other_Functions.Func(Other_Function_Name,*args)
"""


def Func(Bot_Variables):
    pass

