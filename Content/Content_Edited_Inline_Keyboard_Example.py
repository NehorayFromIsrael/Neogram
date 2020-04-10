from Program.Send import Send as Send
from Program.Button import Button as Button


def Func(Bot_Variables):



    Send.Edited_Inline_Keyboard(Bot_Variables, "Text Here",
                            Button.Inline(["u", "URL Button", "www.google.co.il"]),
                            Button.Inline(["c", "Callback Button", "Inline_Example"]),

                            )