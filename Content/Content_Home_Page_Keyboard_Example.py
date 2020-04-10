from Program.Send import Send as Send
from Program.Button import Button as Button

def Func(Bot_Variables):

    
    Send.Keyboard(Bot_Variables, "Markup Keyboard",
              Button.Markup("Deep Navigation Example"),
              Button.Markup("Send Text Message Example", "Send Inline Keyboard Example"), )
