from Program.Send import Send as Send
import configure

def Func(Bot_Variables):

    Mongo_Collections = Bot_Variables[10]


    lowest_users_bot_username = " "

    text = configure.message_when_reach_limit + " " + lowest_users_bot_username
    Send.Message(Bot_Variables,text)
