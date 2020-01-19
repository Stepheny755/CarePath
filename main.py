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

    def refresh(self):
        self.readAllMessages()

    def readAllMessages(self):
        for chat in self.data:
            id=chat[0]
            print(self.api.parseChats())
            if(id==self.api.findChatByMemberName("Stephen")):
                #self.api.sendMessage(id,self.api.writePromptString())
                for message in self.api.readMessage(id):
                    print(message)
                    if '1' in message['message']:
                        pass
                    elif '2' in message['message']:
                        chat[1]=State.SYMP
                        #self.api.sendMessage(chat[0],"Sure, I can help with that. What symptoms do you have?")

                    elif '3' in message['message']:
                        pass
            break

b = Main()

@app.route('/',methods=['POST'])
def post_json():
    data=request.form
    b.refresh()
    print(data)
    return data

Flask.run(app,host="167.99.186.154")
