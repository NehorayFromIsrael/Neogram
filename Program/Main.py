#!/usr/bin/python3

from telegram.ext.dispatcher import run_async
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import Add_User_Info as Add_User_Info
import Program.Inline_Funcs as Inline_Funcs
import Program.Markup_Funcs as Markup_Functions
import Program.Update_Last_Seen_And_UserName as Update_Last_Seen_And_UserName
import Program.Get_Bot_Variables as Get_Bot_Variables
import Message_Handler.Start.Start as START
import Message_Handler.Start.Message_Handler as MES_HANDEL
import Program.Update_Phone as Update_Phone
import Program.Update_Location as Update_Location
import Program.Update_Bot_Asset as Update_Bot_Asset
import configure
import Program.message_when_reach_bot_users_limit as message_when_reach_bot_users_limit
import telegram

#*******************************************************************************************

class Telegram_Bot(object):

    """ this class includes the bot dispatcher(task manager), defenition of start command in the bot and messeage handler"""

    TOKEN = ''


    Bot_Variables = []

    #*******************************************************************************************

    # - Bot Dispatcher (bot task manager) - #
    @classmethod
    def bot_dispatcher(cls):

        # - Creating dispatcher object - #
        updater = Updater(cls.TOKEN,use_context=True,workers=configure.Threads_Per_Bot)
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
        updater.idle()


    # - Start command - #
    @classmethod
    @run_async
    def start(cls,update, context):


        cls.Bot_Variables = Get_Bot_Variables.Func([update,context],cls.TOKEN)

        Mongo_Collections = cls.Bot_Variables[10]
        Users = Mongo_Collections[0]
        Chat_ID = cls.Bot_Variables[1]
        Bot_User = telegram.Bot(cls.TOKEN).get_me()
        Bot_User  = Bot_User["id"]

        user_exist = Users.find({"chat_id":Chat_ID,"bot_user":Bot_User}).count() > 0

        if user_exist :
            START.Func(update, context,cls.TOKEN)

#*******************************************************************************************


    # - Message Handler (Recives messages and decide what to do) - #
    @classmethod
    @run_async
    def Message_Handler(cls,update,context):

        Chat_ID = update["message"]["chat"]["id"]
        Message = update["message"]["text"]
        First_Name = update["message"]["chat"]["first_name"]
        UserName = update["message"]["chat"]["username"]
        Message_ID = update["message"]["message_id"]

        users = configure.collections[0]
        locations = configure.collections[1]


        vars = [ update , context ,Message]

        Markup_Functions.Func(vars)

        # - activate message handler func in message_handller folder - #
        MES_HANDEL.Func(update,context,cls.TOKEN)

        # - update last seen and username - #
        vars = [users,Chat_ID,UserName,First_Name]
        Update_Last_Seen_And_UserName.Func(vars)

        vars = [update,Chat_ID,users]
        Update_Phone.Func(vars)

        vars = [update,Chat_ID,locations]
        Update_Location.Func(vars)

#*******************************************************************************************

