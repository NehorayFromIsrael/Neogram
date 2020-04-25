#!/usr/bin/python3

from telegram.ext.dispatcher import run_async
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import Program.Inline_Funcs as Inline_Funcs
import Program.Markup_Funcs as Markup_Functions
import Program.Update_Last_Seen_And_UserName as Update_Last_Seen_And_UserName
import Program.Get_Bot_Variables as Get_Bot_Variables
import Message_Handler.Start.Start as START
import Message_Handler.Start.Message_Handler as MES_HANDEL
import Program.Update_Phone as Update_Phone
import Program.Update_Location as Update_Location
import time
import threading
import telegram
from Program.Send import Send as Send
import configure
import Program.Update_Bot_Asset as Update_Bot_Asset
import Add_User_Info
import Program.check_if_there_is_bot_that_not_reach_the_limit as cl
import Program.Update_Account_Asset as Update_Account_Asset
#*******************************************************************************************

class Telegram_Bot(object):

    """ this class includes the bot dispatcher(task manager), defenition of start command in the bot and messeage handler"""

    TOKEN = ''


    Bot_Variables = []

    #*******************************************************************************************

    # - Bot Dispatcher (bot task manager) - #
    @classmethod
    def bot_dispatcher(cls):
        global updater





        # - Creating dispatcher object - #
        updater = Updater(cls.TOKEN,use_context=True,workers=32)
        dispatcher = updater.dispatcher


        # - Add Bot Start Command To Dispatcher - #
        start_comm = CommandHandler('start', cls.start)
        dispatcher.add_handler(start_comm)


        # - Add Bot Message Handler Command To Handel Mesagess (Recives messages and decide what to do) - #



        dispatcher.add_handler(MessageHandler(Filters.all, cls.Message_Handler))

        # - Add inline patterns - #
        Inline_Functions_list = Inline_Funcs.Func()



        for i in range(len(Inline_Functions_list)):
            dispatcher.add_handler(CallbackQueryHandler(Inline_Functions_list[i][0], pattern=Inline_Functions_list[i][1]))


        # - Start checking for updates (checking for new messages) - #
        updater.start_polling()

        # - If the program close, stop getting updates - #
        #updater.idle()


    # - Start command - #
    @classmethod
    @run_async
    def start(cls,update, context):

        # - get info - #
        cls.Bot_Variables = Get_Bot_Variables.Func([update,context],cls.TOKEN)

        Update_Account_Asset.Func(cls.Bot_Variables)

        Chat_ID = cls.Bot_Variables[1]

        User_Doc = cls.Bot_Variables[10][0].find_one({"chat_id": Chat_ID})

        this_bot = telegram.Bot(cls.TOKEN).get_me()

        number_of_users_in_this_bot = cls.Bot_Variables[10][0].find({"bot_user":  this_bot["id"]}).count()

        Update_Bot_Asset.Func(cls.Bot_Variables,this_bot)

        # - if user exists in mongo - #
        if User_Doc != None:

            # - if the current bot is the user bot , let him in the bot - #
            if User_Doc["bot_user"] == this_bot["id"]:
                START.Func(update, context)
            # - else send him message whit the bot he is registered with - #
            else:

                bot_user = cls.Bot_Variables[10][0].find_one({"chat_id": Chat_ID})["bot_user"]
                bot_user_name = cls.Bot_Variables[10][2].find_one({"id": bot_user})["username"]
                Send.Message(cls.Bot_Variables,configure.message_when_reach_limit + " @" + bot_user_name)

        # - if user not exists in mongo - #
        else:
            # - if this bot users capacity not reach the limit - #
            if number_of_users_in_this_bot < configure.Users_Per_Bot:
                cls.Bot_Variables[13].append(this_bot["id"])
                Add_User_Info.Func(cls.Bot_Variables)
                START.Func(update, context)


            else:

                # - check if there is a bot that not reach the limit - #
                check = cl.Func(cls.Bot_Variables)
                if check[0]:
                    Send.Message(cls.Bot_Variables,configure.message_when_reach_limit + " @" + check[1])
                # - if all bots reach limits - #
                else:
                    cls.Bot_Variables[13].append(this_bot["id"])
                    Add_User_Info.Func(cls.Bot_Variables)
                    START.Func(update, context)



#*******************************************************************************************

    # - Message Handler (Recives messages and decide what to do) - #
    @classmethod
    @run_async
    def Message_Handler(cls,update,context):

        cls.Bot_Variables = Get_Bot_Variables.Func([update,context],cls.TOKEN)
        Markup_Functions.Func(cls.Bot_Variables)


        MES_HANDEL.Func(update,context)
        # - update last seen and username - #
        Update_Last_Seen_And_UserName.Func(cls.Bot_Variables)

        Update_Phone.Func(cls.Bot_Variables)
        Update_Location.Func(cls.Bot_Variables)

        # - If the message equal to STOP, stop getting updates - #
        User_Privileges = cls.Bot_Variables[8]
        Message = cls.Bot_Variables[4]

        if Message == "STOP" and User_Privileges == "root":
            updater.stop()

        context.args = cls.TOKEN

#*******************************************************************************************

