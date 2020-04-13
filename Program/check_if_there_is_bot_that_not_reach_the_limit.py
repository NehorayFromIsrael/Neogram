import configure

def Func(Bot_Variables):
    Bot_Variables = ["771941522:AAGpG71f6B50Kch2QANTihxyKwdImWWmHB8"]

    TOKEN = Bot_Variables[0]

    Mongo_Collections = configure.collections
    Users = Mongo_Collections[0]
    Assets = Mongo_Collections[2]

    this_bot = Assets.find_one({"TOKEN":TOKEN})["id"]

    bots = Users.distinct("bot_user")
    users_each_bot = []

    for i in range(len(bots)):

        users_count = Users.find({"bot_user":bots[i]}).count()
        users_each_bot.append(users_count)

    min_value = min(users_each_bot)

    for x in range(len(users_each_bot)):
        if int(min_value) == int(users_each_bot[i]):
            min_value_place = i


    if this_bot == bots[min_value_place]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(Func("j"))