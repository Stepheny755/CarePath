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
        for i in self.api.parseChats():
            print(i)
            print()
        #print(self.api.parseChats())
        self.state = State.READY




if(__name__=="__main__"):
    b = Bot()
