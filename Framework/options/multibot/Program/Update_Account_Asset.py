import configure




def Func(Bot_Variables):



    Mongo_Collections = Bot_Variables[10]
    Assets = Mongo_Collections[2]
    accounts = configure.TOKENS

    for i in range(len(accounts)):
        account = {
            "type": "telegram account",
            "phone": accounts[i]["phone"],
            "password": accounts[i]["password"],
            "chat_id": ""

        }

        check_if_exist = Assets.find({"phone":accounts[i]["phone"]}).count()>0

        if (not check_if_exist ) and (accounts[i]["phone"] != ""):

            Assets.insert_one(account)


