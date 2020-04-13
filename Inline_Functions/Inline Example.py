import Program.Get_Bot_Variables as Get_Bot_Variables
from Program.Send import Send as Send
from Program.Button import Button as Button

def Func(update,context):

    Bot_Variables = Get_Bot_Variables.Func([update,context])


    print(Bot_Variables)

    Send.Message(Bot_Variables,"hello")

    Send.Edited_Inline_Keyboard(Bot_Variables, "Text Here",
                                Button.Inline(["u", "URL Button", "www.google.co.il"]),
                                Button.Inline(["c", "Press", "Inline Example"]))
