from datetime import date
import Program.Get_Houer as Time

def Func(Bot_Variables):

    try:
        Update = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]

        Mongo_Locations = Bot_Variables[2]



        user_location = {
            "chat_id": Chat_ID,
            "date":date.today().strftime("%d/%m/%Y"),
            "time":Time.Get_Houer(),
            'longitude':Update["message"]["location"]['longitude'],
            'latitude' : Update["message"]["location"]['latitude']
        }


        Mongo_Locations.insert_one(user_location)


    except:
        pass
