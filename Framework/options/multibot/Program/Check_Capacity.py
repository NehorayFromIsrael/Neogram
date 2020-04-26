from Program.Send import Send as Send
import configure
def Func(Bot_Variables):
    Users = Bot_Variables[10][0]

    Users_count = Users.find({}).count()

    capacity = len(configure.TOKENS) * configure.Users_Per_Bot

    capacity_presents = (int(Users_count) / int(capacity)) * 100



    if capacity_presents > float(configure.presents):

        chat_ids = Users.find({"user privileges":"root"})
        chat_ids_count = Users.find({"user privileges":"root"}).count()

        for i in range(chat_ids_count):

            Send.Message([Bot_Variables[0],chat_ids[i]["chat_id"]],"bots users capacity has reach " + str(float(capacity_presents)) + "%\n Users "+ str(Users_count)+ "/" + str(capacity))



