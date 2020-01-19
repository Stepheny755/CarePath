import requests,json

class API():

    accessToken=''
    cse=''
    cid=''
    scope=''
    authorization=''
    basicAuthorization=''
    username='moosemd'
    password='asdf1234$'

    oauthuri='https://api-prod.hypercare.com/oauth/token'
    chaturi='https://api-prod.hypercare.com/graphql/private'

    def __init__(self):
        self.readClientIDSecret()
        self.getAccessToken()
        self.authorization="Bearer "+self.accessToken
        self.basicAuthorization="Basic"+self.basicAuth

    def readClientIDSecret(self):
        f = open("keys/hypercare.txt","r+")
        self.cid=f.readline()
        self.cse=f.readline()
        self.scope=f.readline().strip()
        self.basicAuth=f.readline().strip()

    def getAccessToken(self):
        payload={'grant_type':'password','username':self.username,'password':self.password}
        headers={'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic dW9mdGhhY2tzdGVhbTQ6cGpVY0NGZTRCN0xk'}
        jsondata = requests.post(self.oauthuri,headers=headers,data=payload)
        self.accessToken=(json.loads(jsondata.text)['response']['accessToken'])

    def getUserData(self):
        payload =  "{\"query\":\"query organizationChats($continuationId: ID, $limit: Int, $isPriority: Boolean) {\\r\\n  chatsForOrganization(continuationId: $continuationId, limit: $limit, isPriority: $isPriority) {\\r\\n    chats {\\r\\n      ...basicChatFields\\r\\n    }\\r\\n  }\\r\\n}\\r\\n\\r\\nfragment basicChatFields on Chat {\\r\\n  id\\r\\n  title\\r\\n  type\\r\\n  members {\\r\\n    ...chatMemberFields\\r\\n  }\\r\\n  lastMessage {\\r\\n    ...messageFields\\r\\n  }\\r\\n  lastUnreadMessage {\\r\\n    ...messageFields\\r\\n  }\\r\\n  unreadPriorityMessages\\r\\n  muted\\r\\n  dateCreated\\r\\n  isArchived\\r\\n}\\r\\n\\r\\nfragment chatMemberFields on ChatMember {\\r\\n  id\\r\\n  firstname\\r\\n  lastname\\r\\n  username\\r\\n  role\\r\\n  profilePic {\\r\\n    url\\r\\n  }\\r\\n  status\\r\\n  privilege\\r\\n  workStatus\\r\\n  statusDescription\\r\\n  workStatusProxy {\\r\\n    ...publicUserStatusFields\\r\\n  }\\r\\n}\\r\\n\\r\\nfragment messageFields on Message {\\r\\n  id\\r\\n  priority\\r\\n  message\\r\\n  image\\r\\n#   attachment {\\r\\n#     url\\r\\n#     mimeType\\r\\n#     fileName\\r\\n#   }\\r\\n  type\\r\\n  dateCreated\\r\\n  sender {\\r\\n    ...publicUserFields\\r\\n  }\\r\\n  deliveredTo {\\r\\n    ...deliveryReceiptFields\\r\\n  }\\r\\n  readBy {\\r\\n    ...readReceiptFields\\r\\n  }\\r\\n  data {\\r\\n    __typename\\r\\n    ... on ConsultMessageData {\\r\\n      mrn\\r\\n      firstname\\r\\n      lastname\\r\\n      details\\r\\n    }\\r\\n  }\\r\\n}\\r\\n\\r\\nfragment readReceiptFields on ReadReceipt {\\r\\n  messageId\\r\\n  user {\\r\\n    ...publicUserFields\\r\\n  }\\r\\n  timestamp\\r\\n}\\r\\n\\r\\nfragment deliveryReceiptFields on DeliveryReceipt {\\r\\n  messageId\\r\\n  user {\\r\\n    ...publicUserFields\\r\\n  }\\r\\n  timestamp\\r\\n}\\r\\n\\r\\nfragment publicUserFields on PublicUser {\\r\\n  id\\r\\n  firstname\\r\\n  lastname\\r\\n  username\\r\\n  role\\r\\n  profilePic {\\r\\n    url\\r\\n  }\\r\\n  workStatus\\r\\n  statusDescription\\r\\n  workStatusProxy {\\r\\n    ...publicUserStatusFields\\r\\n  }\\r\\n}\\r\\n\\r\\nfragment publicUserStatusFields on PublicUser {\\r\\n  id\\r\\n  firstname\\r\\n  lastname\\r\\n  username\\r\\n  role\\r\\n  profilePic {\\r\\n    url\\r\\n  }\\r\\n}\",\"variables\":{}}"
        headers={'hypercare-scope':self.scope,'Authorization':self.authorization,'Content-Type': 'application/json'}
        jsondata = requests.post(self.chaturi,headers=headers,data=payload)
        return json.loads(jsondata.text)

    def parseChats(self):
        chatList=self.getUserData()['data']['chatsForOrganization']['chats']
        return chatList

    def findUserID(self):
        payload = "{\"query\":\"query self {\\r\\n    me {\\r\\n        ...FullUserFields\\r\\n    }\\r\\n}\\r\\n\\r\\nfragment FullUserFields on FullUser {\\r\\n    id\\r\\n    firstname\\r\\n    lastname\\r\\n    username\\r\\n    role\\r\\n    profilePic {\\r\\n        url\\r\\n    }\\r\\n    inviteCode\\r\\n}\",\"variables\":{}}"
        headers = {'Authorization':self.authorization,'Content-Type': 'application/json'}
        jsondata = requests.post(self.chaturi,headers=headers,data=payload)
        return json.loads(jsondata.text)['data']['me']['id']


    def findChatByMemberID(self,receiverID):
        for chat in self.parseChats():
            if(chat['type']=='single'):
                if(chat['members'][0]['id']==receiver or chat['members'][1]['id']==receiver):
                    return chat['id']

    def findChatByMemberName(self,receiverName):
        for chat in self.parseChats():
            if(chat['type']=='single'):
                if(chat['members'][0]['firstname']==receiverName or chat['members'][1]['firstname']==receiverName):
                    return chat['id']
        return None

    def findChatByID(self,chatID):
        for chat in self.parseChats():
            if(chat['id']==chatID):
                return chat['id']

    def findOrganizationMembers(self):
        contacts=[]
        payload = "{\"query\":\"query fetchColleagues {\\r\\n    colleagues {\\r\\n        ...GeneralUserFragment\\r\\n    }\\r\\n}\\r\\n\\r\\nfragment GeneralUserFragment on GeneralUser {\\r\\n    id\\r\\n    username\\r\\n    firstname\\r\\n    lastname\\r\\n    role\\r\\n    profilePic {\\r\\n        url\\r\\n    }\\r\\n    status\\r\\n    addresses {\\r\\n        address\\r\\n        type\\r\\n        access\\r\\n        ordinal\\r\\n    }\\r\\n}\",\"variables\":{}}"
        headers = {'hypercare-scope': self.scope,'Authorization': self.authorization,'Content-Type': 'application/json'}
        jsondata = requests.post(self.chaturi,headers=headers,data=payload)
        data = json.loads(jsondata.text)['data']['colleagues']
        for user in data:
            if user['id'] not in contacts:
                contacts.append(user['id'])
        return contacts

    def findNonContactedMembers(self):
        contacts = []
        noncontacts = []
        for user in self.parseChats():
            if(user['type']=='single'):
                data = user['members']
                if data[0]['id'] not in contacts:
                    contacts.append(data[0]['id'])
                if data[1]['id'] not in contacts:
                    contacts.append(data[1]['id'])
        colleagues = self.findOrganizationMembers()
        for member in colleagues:
            if member not in contacts:
                noncontacts.append(member)
        return noncontacts

    def readMessage(self,chatID):
        payload = "{\"query\":\"query fetchMessages ($chatId: ID!, $continuationId: Int, $limit: Int) {\\r\\n    chat(chatId: $chatId) {\\r\\n        messages(continuationId: $continuationId, limit: $limit) {\\r\\n            messages {\\r\\n                ...messageFields\\r\\n            }\\r\\n        }\\r\\n    }\\r\\n}\\r\\nfragment messageFields on Message {\\r\\n    id\\r\\n    priority\\r\\n    message\\r\\n    image\\r\\n    type\\r\\n    attachment {\\r\\n        ...AttachmentFragment\\r\\n    }\\r\\n    dateCreated\\r\\n    sender {\\r\\n        ...publicUserFields\\r\\n    }\\r\\n    deliveredTo {\\r\\n        ...deliveryReceiptFields\\r\\n    }\\r\\n    readBy {\\r\\n        ...readReceiptFields\\r\\n    }\\r\\n    data {\\r\\n        __typename ... on ConsultMessageData {\\r\\n            mrn\\r\\n            firstname\\r\\n            lastname\\r\\n            details\\r\\n        }\\r\\n    }\\r\\n}\\r\\n\\r\\nfragment readReceiptFields on ReadReceipt {\\r\\n    messageId\\r\\n    user {\\r\\n        ...publicUserFields\\r\\n    }\\r\\n    timestamp\\r\\n}\\r\\n\\r\\nfragment deliveryReceiptFields on DeliveryReceipt {\\r\\n    messageId\\r\\n    user {\\r\\n        ...publicUserFields\\r\\n    }\\r\\n    timestamp\\r\\n}\\r\\n\\r\\nfragment publicUserFields on PublicUser {\\r\\n    id\\r\\n    firstname\\r\\n    lastname\\r\\n    username\\r\\n    email\\r\\n    phonenumber\\r\\n    role\\r\\n    profilePic {\\r\\n        url\\r\\n    }\\r\\n    workStatus\\r\\n    statusDescription\\r\\n    workStatusProxy {\\r\\n        ...publicUserStatusFields\\r\\n    }\\r\\n}\\r\\n\\r\\nfragment publicUserStatusFields on PublicUser {\\r\\n    id\\r\\n    firstname\\r\\n    lastname\\r\\n    username\\r\\n    phonenumber\\r\\n    role\\r\\n    profilePic {\\r\\n        url\\r\\n    }\\r\\n}\\r\\n\\r\\nfragment AttachmentFragment on Attachment {\\r\\n    id\\r\\n    url\\r\\n    mimeType\\r\\n    fileName\\r\\n}\",\"variables\":{\"chatId\":\""+chatID+"\"}}"
        headers = {'hypercare-scope': self.scope,'Authorization': self.authorization,'Content-Type': 'application/json'}
        jsondata = requests.post(self.chaturi,headers=headers,data=payload)
        messageList = json.loads(jsondata.text)['data']['chat']['messages']['messages']
        return messageList

    def sendMessage(self,chatID,inputMessage):
        payload = "{\"query\":\"mutation sendMessage($chatId: ID!, $message: String!, $fileId: Int, $type: MessageType, $priority: Boolean) {\\r\\n    chat(chatId: $chatId) {\\r\\n        sendMessage(message: $message, type: $type, fileId: $fileId, priority: $priority) {\\r\\n            id\\r\\n            image\\r\\n            attachment {\\r\\n                ...AttachmentFragment\\r\\n            }\\r\\n            message\\r\\n            type\\r\\n            sender {\\r\\n                id\\r\\n                username\\r\\n            }\\r\\n        }\\r\\n    }\\r\\n}\\r\\n\\r\\nfragment AttachmentFragment on Attachment {\\r\\n    id\\r\\n    url\\r\\n    mimeType\\r\\n    fileName\\r\\n}\",\"variables\":{\"chatId\":\""+chatID+"\",\"message\":\""+inputMessage+"\",\"type\":\"text\",\"priority\":false}}"
        headers={'hypercare-scope':self.scope,'Authorization':self.authorization,'Content-Type': 'application/json'}
        jsondata = requests.post(self.chaturi,headers=headers,data=payload)
        return jsondata.text

    def writePromptString(self):
        promptString = "Hello, how can I help? (1)Nearby HC Services (2)Search Symptoms (3)Regulate Medication"
        return promptString

if(__name__=="__main__"):
    a = API()
    print(a.findUserID())
    #print(a.parseChats()[0])
    #print()
    #print(a.readMessage(a.findChatByMemberName("Stephen")))
    #print(a.getUserData())
