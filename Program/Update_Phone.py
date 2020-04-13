
def Func(Bot_Variables):

    try:
        Update = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]
        Users = Bot_Variables[2]

        Phone = Update["_effective_message"]['contact']['phone_number']

        Users.update_one({"chat_id":Chat_ID},{"$set":{"phone":Phone}})
    except:
        pass

