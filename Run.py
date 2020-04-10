from Program.Main import Telegram_Bot
import configure

"""  run this file to run the telegram bot   """




# - bot token - #
Telegram_Bot.TOKEN = configure.TOKEN




# - start bot task manager - #
Telegram_Bot.bot_dispatcher()
