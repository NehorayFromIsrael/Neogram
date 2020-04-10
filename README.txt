
    --INSTALLATION--

   1. Run this command in this folder to install packages: pip install -r requirements.txt
   2. Download and install MongoDB: https://www.mongodb.com

   * you have to install MongoDB on your machine in order to make all functions available

* run "Run.py" to run bot

* every time user get connected to the bot its save his info inside "Users" collection in mongodb
you can check Add_User_Info file to see what values are saved and also change them



--- configure file ---

in this file you edit the configurations of your bot

1.set your Bot TOKEN

2. add mongodb collections you need to interact whit

3. you can pass more variable to Other_Variables if you wont to easy access from Bot_Variables Array


--- Bot_Variables Array---

 Bot_Variables is an array that stored all bot user info from message, like chat_id,the text of his message etc,
 its store also the MongoDB collections you entered in configure file
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

--- Get_Functions ---

    there is 2 Get_Functions you need to use and they have major job to make the system
    simple and easy to read this is the functions and how to import and used them + explanation how the work:

   Get_Content(Bot_Variables,Content_Name) , "import Program.Get_Content as Get_Content"
   Get_Other_Functions.Func(Other_Function_Name,*args) , "import Program.Get_Other_Functions as Get_Other_Functions"

   When you create a file inside Content folder or Other_Functions folder in order to activate the func inside one of the files
   you dont need to import them individual you only need to use one of the get functions and pass the name of the file you need(no .py included  extension )
   to activate and it will be done dynamically and automatically ,no need for import and run  individual



--- System Structure & Logic ---

the main folder includes 5 additional folders to store functions, there is a specific use for ech folder:

Content = in this you store the "content" functions, what is a content function? every functions that use the Send class
like Send.Message , Send.Keyboard etc, in short every functions that interact directly whit the bot user.

when you add file to this folder to activate the function that inside the file you will use:
Get_Content.Func(Bot_Variables,"name of the file in content folder not include .py  extension") you can import this by use "from import Program.Get_Content as Get_Content"


Inline_Functions = in this folder you put every functions you wont to attached to inline callback button,
the name of the func will be the name of the file(no .py included  extension )

Message_Handler = in this folder you put the functions that runs every time user sends message to the bot,
example: if you craeted a file whit the name "hey" inside the file you write fucntion thats send message whit the string "hello", every time user sends the file name in a message (no .py includ)
the function of the file is activate , in our case sends the message "hello", the bot automatecly activate any function in this folder base if file name equal to user message 

	there is anotehr folder inside "Message_Handler", called "start" whit two files  start.py and Message_Handker.py,
	start.py = every fucntion you write inside will run when bot user send the command "/start" (or when the bot first lunch by the user)
	Message_Handker.py =  every fucntion you write inside will run each time user send message


Other_Functions = every other function you may create for your bot that dont have a special folder stored here,
to activate functions from this folder simply import: "import Program.Get_Other_Functions as Get_Other_Functions"
and use this functions by passing the file name you crated (no .py include) Get_Other_Functions.Func(Other_Function_Name,*args)
you can also pass variables in args

Program = in this folder all the important file of the system are located its better not to edit anything inside this folder


for every folder that stored custom functions there is a template + examples inside, use them!


--- Send Class ---

 all the send functions , use them only in content functions to make all you system well organized

# -In order to use Send Functions you have to import Send module: "from Program.Send import Send as Send" - #
# -In order to use Button Functions you have to import Button module: "from Program.Button import Button as Button" - #


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


Send.Forword(Bot_Variables,from_chat_id,to_chat_id,message_id)


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






