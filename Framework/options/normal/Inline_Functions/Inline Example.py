import Program.Get_Bot_Variables as Get_Bot_Variables
from Program.Send import Send as Send
from Program.Button import Button as Button
import threading

def Func(update,context):

    threading.Thread(target=Your_Code,args=(update,context)).start()


def Your_Code(update,context):

    Bot_Variables = Get_Bot_Variables.Func([update,context])


    Send.Message(Bot_Variables,"hello")


    Send.Edited_Inline_Keyboard(Bot_Variables, "Text Here",
                                Button.Inline(["c", "Alert", "Alert"]),
                                Button.Inline(["c", "Answer", "Answer"]))
