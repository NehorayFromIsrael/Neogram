from datetime import date
import Program.Get_Houer as Time

def Func(Bot_Variables):

    Users_Mongo = Bot_Variables[10][0]
    Chat_ID = Bot_Variables[1]
    UserName = Bot_Variables[3]
    First_Name = Bot_Variables[2]

    # - Update username recored - #
    Users_Mongo.update_one({"chat_id": Chat_ID}, {"$set": {"first_name": First_Name}})

    Users_Mongo.update_one({"chat_id": Chat_ID}, {"$set": {"user_name": UserName}})

    # - Update last seen - #
    Users_Mongo.update_one({"chat_id":Chat_ID}, {"$set":{"last_seen.date":date.today().strftime("%d/%m/%Y"), "last_seen.time":Time.Get_Houer()}})
