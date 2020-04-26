from Program.Main import Telegram_Bot
import configure
import Program.install as install
import ctypes, os
import threading
import Program.Update_Account_Asset as Update_Account_Asset
import Program.Update_Bot_Asset as Update_Bot_Asset

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

for j in range(len(TOKENS)):
    for z in range(len(TOKENS[j]["tokens"])):
        this_bot = telegram.Bot(TOKENS[j]["tokens"][z]).get_me()
        bot_var = [TOKENS[j]["tokens"][z],"","","","","","","","","",configure.collections]
        Update_Bot_Asset.Func(bot_var,this_bot)

Update_Account_Asset.Func(bot_var)


Assets = configure.Mongo_Assets.find({})
len_assets = configure.Mongo_Assets.find({}).count()

for i in range(len_assets):

    if Assets[i]["type"] == "bot":
        threading.Thread(target=Run_BOT, args=(str(Assets[i]["TOKEN"]))).start()


    
    
