from Program.Main import Telegram_Bot
import configure
import Program.install as install
import ctypes, os
import threading

"""  run this file to run the telegram bot   """


def Run_BOT(*args):

    TOKEN = ""
    TOKEN = TOKEN.join(args)
    # - bot token - #
    Telegram_Bot.TOKEN = TOKEN

    # - start bot task manager - #
    Telegram_Bot.bot_dispatcher()


try:
    import telegram.ext
    import telegram
    import pymongo

except:

    try:
        is_admin = os.getuid() == 0
    except AttributeError:
         is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    
    if is_admin == True:
         install.Func()
    else:
        print(" its your first time to run the bot on this machine you have to run as administrator in order to install requierments")

TOKENS = configure.TOKENS


for i in range(len(TOKENS)):
    for x in range(len(TOKENS[i]["tokens"])):
        T = TOKENS[i]["tokens"][x]

        threading.Thread(target=Run_BOT, args=(str(T))).start()


    
    
