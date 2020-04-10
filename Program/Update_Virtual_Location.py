


def Func(Bot_Variables):

    Chat_ID = Bot_Variables[1]
    Message = Bot_Variables[4]
    Users = Bot_Variables[10][0]

    # - Insert message value to virtual location field - #
    Users.update_one({"chat_id":Chat_ID},{"$set":{"virtual_location":Message}})
