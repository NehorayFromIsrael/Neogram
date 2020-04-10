import Program.Get_Content as Get_Content
import Program.Get_Other_Functions as Get_Other_Functions
import Program.Get_Bot_Variables as Get_Bot_Variables
import time
# - use this template to create functions in your bot , variables and functions are listed down below - #
# - its highly recommended not to change any line from this template (just add your code down below, dont edit any existing lines) - #

def Func(update,context):

    Bot_Variables = Get_Bot_Variables.Func([update,context])

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

    * in order to use "Get_Other_Functions.Func(Other_Function_Name,*args)" you have to import this module: "import Program.Get_Other_Functions as Get_Other_Functions"
    """

    Get_Content.Func(Bot_Variables, "Content_Message_Text_Example")


