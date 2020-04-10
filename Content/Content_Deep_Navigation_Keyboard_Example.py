from Program.Send import Send as Send
from Program.Button import Button as Button



def Func(Bot_Variables):

    Send.Keyboard(Bot_Variables, "Text Here",
                  
                Button.Markup( Button.Markup_Location("Send Location")),
                  Button.Markup( Button.Markup_Phone("Send Phone") ),
                    Button.Markup("Go Back To Home Page Example")
                  )


