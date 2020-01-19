from api import API
from waits import Waits
from map import Map
from enum import Enum
from flask import Flask,request
import json

app = Flask(__name__)

class State(Enum):
    READY=0
    LOCA=1
    SYMP=2
    ALRT=3

class Main():

    one = 0
    two = 0
    three = 0
    counter = 0

    def __init__(self):
        self.api = API()
        self.data = []
        self.myID = self.api.findUserID()
        for chat in self.api.parseChats():
            temp = []
            temp.append(chat['id'])
            temp.append(State.READY)
            self.data.append(temp)
        print(self.data)
        self.readAllMessages()

    def readAllMessages(self):
        for chat in self.data:
            id=chat[0]
            for message in self.api.readMessage(id):
                print(message['sender']['id']+": "+message['message'])
                if chat[1]==State.READY:
                    #self.api.sendMessage(id,self.api.writePromptString())
                    mainControl()
                '''if '1' in message['message']:
                    chat[1]=State.LOCA
                elif '2' in message['message']:
                    chat[1]=State.SYMP
                    #self.api.sendMessage(chat[0],"Sure, I can help with that. What symptoms do you have?")
                elif '3' in message['message']:
                    chat[1]=State.ALRT'''

    def incrementCounter(self):
        counter+=1

    def mainControl(self):
        id=self.api.findChatByMemberName("Stephen")
        if counter == 0:
            self.api.sendMessage(id,"Hello, I am Moose M.D, a friendly healthcare chatbot. Would you like me to \n(1) Search nearby healthcare services, \n(2) match your symptoms,\n(3) help regulate your medication?")
        elif counter == 1:
            self.api.sendMessage(id,"Sure, I can help you with that. What are your symptoms?")
        elif counter == 2:
            self.api.sendMessage(id,"I understand that you are experiencing cough, fever, and nausea. Am I correct?")
        elif counter == 3:
            self.api.sendMessage(id,"Here are some possible matches: \nFlu = high \nHepatitis A = moderate \nMeasles = low \nWould you like help with anything else?")
        elif counter == 5:
            self.api.sendMessage(id,"Hello, what would you like help with?")
        elif counter == 6:
            self.api.sendMessage(id,"Sure. What medication(s) are you taking?")
        elif counter == 7:
            self.api.sendMessage(id,"What days of the week do you need to take insulin?")
        elif counter == 8:
            self.api.sendMessage(id,"What time of day would you like a reminder text?")
        elif counter == 9:
            self.api.sendMessage(id,"Ok, your next reminder is set for today at 7:00pm. \nWould you like help with anything else?")
        elif counter == 11:
            self.api.sendMessage(id,"Hello, what would you like help with?")
        elif counter == 12:
            self.api.sendMessage(id,"Of course. What is your postal code?")
        elif counter == 13:
            self.api.sendMessage(id,"Here are the nearest healthcare centres and their availability: \nSt. Michaels Hospital: 30 mins wait time \nThe Hospital for Sick Children: 15 mins wait time \nThe Rehab and Wellbeing Centre at Mount Sinai Hospital: 25 mins wait time \nWould you like help with anything else?")
        else:
            counter += 1 #wait for user to send another message.

b = Main()

@app.route('/',methods=['POST'])
def post_json():
    data=request.form
    b.incrementCounter()
    print(data)
    return data

Flask.run(app,host="167.99.186.154")
