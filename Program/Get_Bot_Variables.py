import Program.Find_File_ID as Find_File_ID
import configure
import Add_User_Info as Add_User_Info
import telegram
import Program.Update_Bot_Asset as Update_Bot_Asset
import Program.message_when_reach_bot_users_limit as message_when_reach_bot_users_limit
import Program. check_if_there_is_bot_that_not_reach_the_limit as  check_if_there_is_bot_that_not_reach_the_limit

def Func(update,*args):


    context = update[1]
    update = update[0]



    # - get user info - #

    try:

        Json_Message = update["message"]
        Chat_ID = update["message"]["chat"]["id"]
        Message = update["message"]["text"]
        First_Name = update["message"]["chat"]["first_name"]
        UserName = update["message"]["chat"]["username"]
        Message_ID = update["message"]["message_id"]
        File_ID = Find_File_ID.Func(Json_Message)

    except:

        Json_Message = update["callback_query"]["message"]
        Chat_ID = update["callback_query"]["message"]["chat"]["id"]
        Message = update["callback_query"]["message"]["text"]
        First_Name = update["callback_query"]["message"]["chat"]["first_name"]
        UserName = update["callback_query"]["message"]["chat"]["username"]
        Message_ID = update["callback_query"]["message"]["message_id"]
        File_ID = Find_File_ID.Func(Json_Message)

    # - get mongo collections - #
    Mongo_Collections = configure.collections

    Users = Mongo_Collections[0]
    Assets = Mongo_Collections[2]


    # - get bot TOKEN - #
    if len(args) != 0:
        TOKEN = args[0]
    else:

        bot_id = Users.find_one({"chat_id":Chat_ID})
        bot_id = bot_id["bot_user"]

        TOKEN = Assets.find_one({"id":bot_id})
        TOKEN = TOKEN["TOKEN"]




    # - get user info from mongo - #


    User_Doc = Mongo_Collections[0].find_one({"chat_id": Chat_ID})

    if User_Doc == None or Message == "/start":

        Bot_Variables = [TOKEN, Chat_ID, First_Name, UserName, Message, Message_ID, File_ID,
                         None, None, None, Mongo_Collections,
                         Json_Message, update, configure.Other_Variables, context, telegram.Bot(TOKEN).get_me()]

        Bot_User = Bot_Variables[15]["id"]

        users_in_this_bot = Mongo_Collections[0].find({"bot_user": Bot_User}).count()

        check = check_if_there_is_bot_that_not_reach_the_limit.Func(Bot_Variables)

        check_if_user_id_in_mongo = Mongo_Collections[0].find({"chat_id": Chat_ID}).count() >0

        # - if users limit per bot greater then current number of users in bot - #
        if configure.Users_Per_Bot > users_in_this_bot or configure.Users_Per_Bot == 0 or check == True and check_if_user_id_in_mongo == False:

            # - save user information in database - #
            Add_User_Info.Func(Bot_Variables)

            # - and then get user info from mongo - #
            User_Doc = Mongo_Collections[0].find_one({"chat_id": Chat_ID})

            # - update bot asset in mongo assets - #
            Update_Bot_Asset.Func(Bot_Variables)


        else:
            message_when_reach_bot_users_limit.Func(Bot_Variables)


    Bot_Variables = [TOKEN, Chat_ID, First_Name, UserName, Message, Message_ID, File_ID,
                         User_Doc["virtual_location"], User_Doc["user privileges"], User_Doc["language"], Mongo_Collections,
                         Json_Message, update, configure.Other_Variables,context]


    return Bot_Variables


if __name__ == "__main__":
    m = {'update_id': 146187526, 'message': {'message_id': 695, 'date': 1585821699, 'chat': {'id': 42155571, 'type': 'private', 'username': 'Neo2222', 'first_name': 'ℕ'}, 'text': 'g', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 42155571, 'first_name': 'ℕ', 'is_bot': False, 'username': 'Neo2222', 'language_code': 'he'}}, '_effective_user': {'id': 42155571, 'first_name': 'ℕ', 'is_bot': False, 'username': 'Neo2222', 'language_code': 'he'}, '_effective_chat': {'id': 42155571, 'type': 'private', 'username': 'Neo2222', 'first_name': 'ℕ'}, '_effective_message': {'message_id': 695, 'date': 1585821699, 'chat': {'id': 42155571, 'type': 'private', 'username': 'Neo2222', 'first_name': 'ℕ'}, 'text': 'g', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 42155571, 'first_name': 'ℕ', 'is_bot': False, 'username': 'Neo2222', 'language_code': 'he'}}}

    u = {'update_id': 146187609, 'callback_query': {'id': '181056802259502322', 'chat_instance': '-5620424812332190766', 'message': {'message_id': 731, 'date': 1585825030, 'chat': {'id': 42155571, 'type': 'private', 'username': 'Neo2222', 'first_name': 'ℕ'}, 'text': 'Inline Keyboard', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'reply_markup': {'inline_keyboard': [[{'text': 'URL Button', 'url': 'https://www.google.co.il/'}, {'text': 'FUNC Button', 'callback_data': 'Template'}]]}, 'from': {'id': 771941522, 'first_name': 'טלטרמפ🚗 - חפש אשר וסע!🙆\u200d♂️', 'is_bot': True, 'username': 'TeletrempBot'}}, 'data': 'Template', 'from': {'id': 42155571, 'first_name': 'ℕ', 'is_bot': False, 'username': 'Neo2222', 'language_code': 'he'}}, '_effective_user': {'id': 42155571, 'first_name': 'ℕ', 'is_bot': False, 'username': 'Neo2222', 'language_code': 'he'}, '_effective_chat': {'id': 42155571, 'type': 'private', 'username': 'Neo2222', 'first_name': 'ℕ'}, '_effective_message': {'message_id': 731, 'date': 1585825030, 'chat': {'id': 42155571, 'type': 'private', 'username': 'Neo2222', 'first_name': 'ℕ'}, 'text': 'Inline Keyboard', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'reply_markup': {'inline_keyboard': [[{'text': 'URL Button', 'url': 'https://www.google.co.il/'}, {'text': 'FUNC Button', 'callback_data': 'Template'}]]}, 'from': {'id': 771941522, 'first_name': 'טלטרמפ🚗 - חפש אשר וסע!🙆\u200d♂️', 'is_bot': True, 'username': 'TeletrempBot'}}}

    print(Func(u))