import Program.Connect_To_Mongo as Mon



# - SET BOTS TOKENS - #
# - all tokens in every account list will run  by threads (in the same time)- #
# the phone and password are optional, its only to keep track on your telegram accounts in the database

TOKENS = [
    {"phone": "+972549331207", "password": "","tokens": ["771941522:AAGpG71f6B50Kch2QANTihxyKwdImWWmHB8"]}

]

TOKEN = TOKENS[0]["tokens"][0]

# - set users limit per bot - #
Users_Per_Bot = 0

# - edit what message user get if he enter to bot thats reach limit - #
# - the message will send + username of bot whit lowest users - #
message_when_reach_limit = "this bot has reach full capacity please enter this link"

# - notify when users capacity reach this presents - #
presents = 80

# - choose how to send message when reach limit , the value of user_privileges of user - #
send_to = "root"

#_______________________________________________________#
# - SET DATABASES - #

# - database names list - #
Database_Name = ["Telegram_Bot"]


# - get collections use func: Mon.Func(Database_Name,Collection_Name) - #
Mongo_Users = Mon.Func(Database_Name[0], "Users")
Mongo_Locations = Mon.Func(Database_Name[0], "Locations")
Mongo_Assets = Mon.Func(Database_Name[0], "Assets")



# - Add mongo collections to list - #
collections = [Mongo_Users,Mongo_Locations,Mongo_Assets]

#_______________________________________________________#

# - PASS OTHER VARIABLES INSIDE "Bot_Variables" ARREY

Other_Variables = []