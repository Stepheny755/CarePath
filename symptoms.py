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
         
        print(lenSymp)
        for i in range(numIssues):
            percents.append(100*(((0.6)*counter[topBad[i]]/len(userMessage))+((0.4)*counter[topBad[i]]/lenSymp[topBad[i]])))
            print(percents[i])
            if percents[i]>=70:
                percents[i]="likely"
            elif percents[i]>=40:
                percents[i]="moderately likely"s
            else: 
                percents[i]="unlikely"
        
        for x in healthIssues.keys():
            copyKeys.append(x);

        topIssues=[]

        for x in range(numIssues):
            topIssues.append(copyKeys[topBad[x]])
        
        outputDisease = "Possible matches to your symptoms are: "
        outputPercents = "(sickness = likelihood): \n"
        for x in range(len(topIssues)):
         outputDisease += topIssues[x]+ " "
         outputPercents += percents[x]+ "\ns"
        #print(topIssues)
        #print(percents)
   
        
        
    
    def readFile(self,fileName):

        healthIssues={}
        with open(fileName) as f:
 
            for line in f:
                line = line.replace("\r", "").replace("\n", "")
                key,val =line.split(",")    
                val=val.split("/")
                healthIssues[key]=val
                
        self.compare(healthIssues)
              
userMessage=["fever","headache","dizziness","nausea"]     
chat=Chat(userMessage)
chat.readFile(r"assets/symptoms.txt")




