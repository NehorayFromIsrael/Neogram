
def Func(Bot_Variables):

    try:
        Update = Bot_Variables[12]
        Chat_ID = Bot_Variables[1]

        Mongo_Collections = Bot_Variables[10]
        Users = Mongo_Collections[0]

        Phone = Update["_effective_message"]['contact']['phone_number']

        Users.update_one({"chat_id":Chat_ID},{"$set":{"phone":Phone}})
    except:
        pass

