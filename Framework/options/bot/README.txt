
**** first install MongoDB on your system ****

**** run "Run.py" file to run bot ****

**** if its first time you run this bot on your machine it may take
 a couple of minutes to install the requirements **** 

**** if your machine uses linux os and its your first time to run bot in the system 
you shuld use "sudo" to run "Run.py" in oeder to install requirements ****

Also if you using linux make sure to run in python 3 

**** if you getting error for requirements installation , please see install.py file 
inside Program folder to install requirements manually ****




**** every time user join to the bot its save his info inside "Users" collection in mongodb 
you can check Add_User_Info file to see what values are saved and also change them ****


**** every time user send message his "last_seen" value in mongodb "Users" collection is updated ****

**** every time user pressed on send phone button (Button.Markup_Phone("send phone"))  his "phone" value in mongodb "Users" collection is updated ****

**** every time user pressed on send location button (Button.Markup_Location("send location"))  his "location info" value in mongodb "Location" collection is updated ****





--- configure.py file ---

in this file you edit the configurations of your bot

1.set your Bot TOKEN

2. add mongodb collections you need to interact whit

3. you can pass more variable to Other_Variables if you wont to easy access from Bot_Variables Array


--- Bot_Variables Array---

 Bot_Variables is an array that stored all bot user info from message, like chat_id,the text of his message etc,
 its store also the MongoDB collections you entered in "configure file"
 and also other variable you may wont to pass also configured in "configure" file

 you have easy access from any func to all the variables you ever need for your bot

    TOKEN = Bot_Variables[0]
    Chat_ID = Bot_Variables[1]
    First_Name = Bot_Variables[2]
    UserName = Bot_Variables[3]
    Message = Bot_Variables[4]
    Message_ID = Bot_Variables[5]
    File_ID = Bot_Variables[6]
    Virtual_Location = Bot_Variables[7]
    User_Privileges = Bot_Variables[8]
    User_Lang = Bot_Variables[9]
    Mongo_Collections = Bot_Variables[10]
    Json_Message = Bot_Variables[11]
    Update = Bot_Variables[12]
    Other_Variables = Bot_Variables[13]
    Context = Bot_Variables[14]



--- Message_Handler (folder) ---
	
 in this folder you put the functions that runs every time user sends message to the bot,
example: if you craeted a file whit the name "hey" inside the file you write fucntion thats send message whit the string "hello", every time user sends the file name in a message (no .py includ)
the function of the file is activate , in our case sends the message "hello", the bot automatecly activate any function in this folder base if file name equal to user message 

if you wont to create function that will run whit more then one word , in the file name use "#" character to seperate between the words,
example: we create file whit the name "a#b.py" every time the user send the message "a" or "b" the fun inside the file will run.


there is anotehr folder inside "Message_Handler", called "start" whit two files  start.py and Message_Handler.py,

start.py = every fucntion you write inside will run when bot user send the command "/start" (or when the bot first lunch by the user)
Message_Handler.py =  every fucntion you write inside will run each time user send message



--- Inline_Functions (folder) ---

in this folder you put every functions you wont to attached to inline callback button,
the name of the func will be the name of the file(no .py included  extension )


--- Other_Functions (folder) ---

every other function you may create for your bot that dont have a special folder stored here.


--- Program (folder) ---

in this folder all the important file of the system are located, its better not to edit anything inside this folder if you don't know what you doing.






**** for every folder that stored custom functions there is a template + examples inside, use them ! ****





    ---- imports ----

    from Program.Send import Send as Send

    from Program.Button import Button as Button




    --- Send Class ---


Send.Message(Bot_Variables,"Paste Text Here")

Send.Keyboard(Bot_Variables, "Text Here",
                  Button.Markup("button 1"),
                  Button.Markup(Button.Markup_Location("Send_Location")),
                  Button.Markup( Button.Markup_Phone("Send_Phone") , "button 5", "button 6"))



#NOTE: when when you used Button.Inline() for creating buttons for inline keyboard this is the syntax:
# ["URL/CALLBACK Button type( u/c )","button text","the url or callback name"]
# the callback name is the name you gave to the file you created in "Inline_Function" folder (not include the .py extinction)

Send.Inline_Keyboard(Bot_Variables, "Text Here" ,
                         Button.Inline(  ["U","URL Button","https://www.google.co.il/"] ,  ["C","Callback Button","Template"] ) ,
                         Button.Inline(["C","Callback Button","Template"] ,["U","URL Button","https://www.google.co.il/"])
                         )

# send edited keyboard, its edit current inline keyboard and change buttons give deep navigation effect

Send.Edited_Inline_Keyboard(Bot_Variables,"Text Here",
                            Button.Inline(["u","URL Button","www.google.co.il"])
                            )


Send.Callback_Answer(Bot_Variables,"Callback Query Answer")

Send.Callback_Alert(Bot_Variables,"Callback Query Alert")

Send.Forword(Bot_Variables,from_chat_id,to_chat_id,message_id)


# send any file by file id , type : video/voice message/photo/document/sticker
Send.Any_File(Bot_Variables,file_id,caption)


--- Buttons Types ---

# regular markup button
Button.Markup("button text1","button text2")

# make button markup to send user location
Button.Markup_Location("button text")

# make button markup to send user phone number
Button.Markup_Phone("button text")

# regular inline button
Button.Inline( ["URL/CALLBACK Button type( u/c )","button text","the url or callback name"])

#syntax:

* each time activated gives 1 rows of buttons


#Markup synatx
Send.Keyboard(Bot_Variables, "Text Here",
                  Button.Markup("button 1"),
                  Button.Markup(Button.Markup_Location("Send_Location")),
                  Button.Markup( Button.Markup_Phone("Send_Phone") , "button 5", "button 6"))


#Inline synatx
#NOTE: when when you used Button.Inline() for creating buttons for inline keyboard this is the syntax:
# ["URL/CALLBACK Button type( u/c )","button text","the url or callback name"]
# the callback name is the name you gave to the file you created in "Inline_Function" folder (not include the .py extinction)

Send.Inline_Keyboard(Bot_Variables, "Text Here" ,
                         Button.Inline(  ["U","URL Button","https://www.google.co.il/"] ,  ["C","Callback Button","Template"] ) ,
                         Button.Inline(["C","Callback Button","Template"] ,["U","URL Button","https://www.google.co.il/"])
                         )


