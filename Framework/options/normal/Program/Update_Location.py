from datetime import date
import Program.Get_Houer as Time

def Func(Bot_Variables):

    try:
        Update = Bot_Variables[12]
        Chat_ID = Bot_Variables[1]

        Mongo_Collections = Bot_Variables[10]
        Mongo_Locations = Mongo_Collections[1]

        Location = Update["message"]["location"]


        user_location = {
            "chat_id": Chat_ID,
            "date":date.today().strftime("%d/%m/%Y"),
            "time":Time.Get_Houer(),
            'longitude':Update["message"]["location"]['longitude'],
            'latitude' : Update["message"]["location"]['latitude']
        }

        print(user_location)

        Mongo_Locations.insert_one(user_location)


    except:
        pass
