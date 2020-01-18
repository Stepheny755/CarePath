import json

class Chat:
   
    def __init__(self, userMessage):
        self.userMessage = userMessage
                      
    def compare(self,healthIssues):
        
        counter = [0 for i in range(len(healthIssues))]
        lenSymp = [0 for i in range(len(healthIssues))]
        numIssues =3;
        for x in userMessage:
            pos = 0
            for k,v in healthIssues.items():
                lenSymp[pos] = len(v)
                for symp in v:
                    if x == symp:
                        counter[pos] += 1
                        
                pos+=1

        topBad = sorted(range(len(counter)), key = lambda k: counter[k])
        topBad.reverse()
        percents = []
        copyKeys=[]

        for i in range(3):
            percents.append(counter[topBad[i]]/lenSymp[topBad[i]]*100)
        
        for x in healthIssues.keys():
            copyKeys.append(x);

        topIssues=[]

        for x in range(numIssues):
            topIssues.append(copyKeys[topBad[x]])
        
            
                
        print(topIssues)
        print(percents)
        
        
    
    def readFile(self,fileName):

        healthIssues={}
        with open(fileName) as f:
 
            for line in f:
                line = line.replace("\r", "").replace("\n", "")
                key,val =line.split(",")    
                val=val.split("/")
                healthIssues[key]=val
                
        self.compare(healthIssues)
              
userMessage=["sorethroat","headache","fatigue"]     
chat=Chat(userMessage)
chat.readFile(r"C:\Users\arafa\Desktop\test.txt")




