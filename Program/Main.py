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
        updater.idle()


    # - Start command - #
    @classmethod
    @run_async
    def start(cls,update, context):

        START.Func(update, context)

        # - save user information in database - #
        Add_User_Info.Func(cls.Bot_Variables)





#*******************************************************************************************


    # - Message Handler (Recives messages and decide what to do) - #
    @classmethod
    @run_async
    def Message_Handler(cls,update,context):

        cls.Bot_Variables = Get_Bot_Variables.Func([update,context])
        Markup_Functions.Func(cls.Bot_Variables)



        MES_HANDEL.Func(update,context)

        # - update last seen and username - #
        Update_Last_Seen_And_UserName.Func(cls.Bot_Variables)


#*******************************************************************************************

