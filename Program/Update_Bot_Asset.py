
def Func(Bot_Variables):


        TOKEN = Bot_Variables[0]

        Mongo_Collections = Bot_Variables[10]

        Mongo_Assets = Mongo_Collections[2]

        condition = Mongo_Assets.find({"TOKEN":TOKEN}).count() > 0

        Bot = Bot_Variables[15]


        if not condition :

            asset = {
            "type": "bot",
            "TOKEN": TOKEN,
            "id": Bot["id"],
            "name": Bot["first_name"],
            "username":Bot["username"],
            "phone": ""

            }



            Mongo_Assets.insert_one(asset)

