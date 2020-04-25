import configure
def Func(Bot_Variables):

    Bot_Variables = ["771941522:AAGpG71f6B50Kch2QANTihxyKwdImWWmHB8"]


    TOKEN = Bot_Variables[0]

    #Mongo_Collections = Bot_Variables[10]

    Mongo_Collections = configure.collections

    Users = Mongo_Collections[0]
    Assets = Mongo_Collections[2]

    this_bot = Assets.find_one({"TOKEN":TOKEN})["id"]

    #min_users_bot_value =  Assets.find().sort({a: 1}).limit(1)

    bots = Assets.distinct("id")

    bots_count = []
    min_value_place = 0

    for i in range(len(bots)):

        count_bot = Users.find({"bot_user":bots[i]}).count()
        bots_count.append([bots[i],count_bot])

        if i == 0:
            min_value = bots_count[0][1]
        else:
            if min_value > count_bot:
                min_value=count_bot
                min_value_place = i


    if bots_count[min_value_place][1] < configure.Users_Per_Bot:

        min_bot = Assets.find_one({"id":bots_count[min_value_place][0]})["username"]
        return [True,min_bot]
    else:
        min_bot = Assets.find_one({"id":bots_count[min_value_place][0]})["username"]

        return [False,min_bot]



if __name__ == "__main__":
    print(Func("j"))