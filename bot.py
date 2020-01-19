from api import API
from enum import Enum

class State(Enum):
    READY=0
    LOCA=1
    SYMP=2
    ALRT=3

class Bot():
    def __init__(self):
        self.api = API()
        self.data = []
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
            print(self.api.readMessage(id))
            print()


if(__name__=="__main__"):
    b = Bot()
