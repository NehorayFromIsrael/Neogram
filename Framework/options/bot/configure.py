import Program.Connect_To_Mongo as Mon



# - SET BOT TOKEN - #

TOKEN = "771941522:AAGpG71f6B50Kch2QANTihxyKwdImWWmHB8"


#_______________________________________________________#
# - SET DATABASES - #

# - database names list - #
Database_Name = ["Telegram_Bot"]


# - get collections use func: Mon.Func(Database_Name,Collection_Name) - #
Mongo_Users = Mon.Func(Database_Name[0], "Users")
Mongo_Locations = Mon.Func(Database_Name[0], "Locations")


# - Add mongo collections to list - # 
collections = [Mongo_Users,Mongo_Locations]

#_______________________________________________________#

# - PASS OTHER VARIABLES INSIDE "Bot_Variables" ARREY

Other_Variables = []


# - requirements , add to list for automatic req installation- #
req = []

