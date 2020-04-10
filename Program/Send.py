#!/usr/bin/python3
import telegram
import Program.Update_Virtual_Location as Update_Virtual_Location


#todo check all files if ther note ar corrente

#todo save phone and location in database

#todo add text message html format like bold italic etc

#todo make send function can send from url and from disk

# todo create template for all send functions inside the functions folder

#todo create system to run multiply bots

#todo create send function for: video note,telegram.CallbackQuery.answer, and alert message

#todo create documantation for the system in the REaDME file

# todo create example file thats run all the functions inside the inline and markup funcs folders


#*******************************************************************************************
class Send(object):



    """
     class thats has functions to send messages keyboard inline etc in bot.
     everything attach to send somthing in bot

    """


    # - Send message - #
    @staticmethod
    def Message(Bot_Variables,Text):
        TOKEN = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]
        telegram.Bot(TOKEN).send_message(chat_id=Chat_ID, text=Text)

#*******************************************************************************************

    # - Send keyboard - #
    @staticmethod
    def Keyboard(Bot_Variables,Text,*Buttons):

        TOKEN = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]

        Update_Virtual_Location.Func(Bot_Variables)

        Keyboard =  {'keyboard': [],'resize_keyboard': True, 'one_time_keyboard': False, 'selective': False}

        for i in range(len(Buttons)):
            Keyboard["keyboard"].append(Buttons[i])
        telegram.Bot(TOKEN).send_message(chat_id=Chat_ID, text=Text,reply_markup=Keyboard)

#*******************************************************************************************

    # - Send inline keyboard -#
    @staticmethod
    def Inline_Keyboard(Bot_Variables,Text,*Buttons):

        Json_Message = Bot_Variables[11]

        Inline_Keyboard = {'inline_keyboard': [ ]}

        for i in range(len(Buttons)):
            Inline_Keyboard["inline_keyboard"].append(Buttons[i])


        Json_Message.reply_text(Text,reply_markup=Inline_Keyboard)

#*******************************************************************************************

    # - Send Edited inline keyboard -#
    @staticmethod
    def Edited_Inline_Keyboard(Bot_Variables,Text,*Buttons):

        TOKEN = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]
        Message_ID = Bot_Variables[5]

        Inline_Keyboard = {'inline_keyboard': [ ]}

        for i in range(len(Buttons)):
            Inline_Keyboard["inline_keyboard"].append(Buttons[i])

        telegram.Bot(TOKEN).edit_message_text(chat_id=Chat_ID,
                    message_id=Message_ID,
                    text=Text,
                    reply_markup=Inline_Keyboard)

#*******************************************************************************************

    # - Send Sticker -#
    @staticmethod
    def Ssticker(Bot_Variables,file_id):
        TOKEN = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]

        telegram.Bot(TOKEN).send_sticker(chat_id=Chat_ID,sticker=file_id).sticker


    # - Send Document -#
    @staticmethod
    def Document(Bot_Variables, file_id, text=None):
        TOKEN = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]
        telegram.Bot(TOKEN).send_document(Chat_ID, file_id, caption=text)

    @staticmethod
    def Photo(Bot_Variables, file_id, text=None):
        TOKEN = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]
        telegram.Bot(TOKEN).send_photo(Chat_ID, file_id, caption=text)

    @staticmethod
    def Video(Bot_Variables,file_id,text=None):
        TOKEN = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]
        telegram.Bot(TOKEN).send_video(Chat_ID, file_id,caption=text)

    @staticmethod
    def Voice(Bot_Variables,file_id,text=None):
        TOKEN = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]
        telegram.Bot(TOKEN).send_voice(Chat_ID, file_id,caption=text)

    @classmethod
    def Any_File(cls,Bot_Variables,file_id,text=None):
        TOKEN = Bot_Variables[0]
        Chat_ID = Bot_Variables[1]

        try:
            cls.Ssticker(Bot_Variables,file_id)
        except:
            try:
                cls.Document(Bot_Variables, file_id, text)
            except:
                try:
                    cls.Photo(Bot_Variables, file_id, text)
                except:
                    try:
                        cls.Video(Bot_Variables, file_id, text)
                    except:
                        try:

                            cls.Voice(Bot_Variables,file_id,text)
                        except:
                            pass


# *******************************************************************************************

    @staticmethod
    def Forword(Bot_Variables,from_chat_id,to_chat_id,message_id):
        TOKEN = Bot_Variables[0]
        #context = Bot_Variables[14]
        telegram.Bot(TOKEN).forward_message(to_chat_id, from_chat_id, message_id)


if __name__ == "__main__":
    token = ["771941522:AAGpG71f6B50Kch2QANTihxyKwdImWWmHB8","42155571"]


    f_id ='AgACAgQAAxkBAAIQbl6QNEXhXbQvFl6mFqjTHA5co5aiAAKwszEbd4yBUKd80DI5Vg8ijrUGI10AAwEAAwIAA20AAzE0AAIYBA'
    t = None
    Send.Any_File(token,f_id,t)
