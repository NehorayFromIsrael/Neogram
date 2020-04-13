from Program.Main import Telegram_Bot
import configure

"""  run this file to run the telegram bot   """




# - run all bots - #
for i in range(len(configure.TOKEN)):
    # - bot token - #
    Telegram_Bot.TOKEN = configure.TOKEN[i]

    # - start bot task manager - #
    Telegram_Bot.bot_dispatcher()

