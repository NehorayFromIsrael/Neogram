from Program.Send import Send as Send
from Program.Button import Button as Button


def Func(Bot_Variables):
    
    Send.Inline_Keyboard(Bot_Variables, "Inline Keyboard",
                         Button.Inline(["U", "URL Button", "www.google.co.il"],
                                       ["C", "Callback Button", "Inline_Example"]),
                         Button.Inline(["C", "Callback Button", "Inline_Example"],
                                       ["U", "URL Button", "www.google.co.il"])
                         )