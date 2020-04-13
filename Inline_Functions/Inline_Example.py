import Program.Get_Bot_Variables as Get_Bot_Variables
import Program.Get_Content as Get_Content

def Func(update,context):
    Bot_Variables = Get_Bot_Variables.Func([update,context])

    print(Bot_Variables)

    Get_Content.Func(Bot_Variables,"Content_Edited_Inline_Keyboard_Example")


