
def Func(Bot_Variables,Asset):

    TOKEN = Bot_Variables[0]

    Mongo_Collections = Bot_Variables[10]

    Mongo_Assets = Mongo_Collections[2]

    exists = Mongo_Assets.find({"TOKEN": TOKEN}).count() > 0

    Bot = Asset

    if (not exists):
        asset = {
            "type": "bot",
            "TOKEN": TOKEN,
            "id": Bot["id"],
            "name": Bot["first_name"],
            "username": Bot["username"],
            "phone": ""

        }

        Mongo_Assets.insert_one(asset)