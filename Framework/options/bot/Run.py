from Program.Main import Telegram_Bot
import configure
import Program.install as install

"""  run this file to run the telegram bot   """


try:
    import telegram.ext
    import telegram
    import pymongo

except:
    install.Func()

    print(":LKJHGF")
    
# - bot token - #
Telegram_Bot.TOKEN = configure.TOKEN




# - start bot task manager - #
Telegram_Bot.bot_dispatcher()
