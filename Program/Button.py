class Button(object):

    @staticmethod
    def Markup(*Buttons):
        Final_B = []

        for i in range(len(Buttons)):
            Final_B.append(Buttons[i])
        return Final_B

    @staticmethod
    def Inline(*Buttons):

        Final_B = []

        for i in range(len(Buttons)):

            if Buttons[i][0] == "U" or Buttons[i][0] == "u":
                Final_B.append({'text': Buttons[i][1], 'url': Buttons[i][2]})

            if Buttons[i][0] == "C" or Buttons[i][0] == "c":
                Final_B.append({'text': Buttons[i][1], "callback_data": Buttons[i][2]})

        return Final_B


    @staticmethod
    def Markup_Location(Button):
       return {'text': Button, 'request_location': True}

    @staticmethod
    def Markup_Phone(Button):
       return {'text': Button, 'request_contact': True}