import json
import datetime
import datetime as dt
from datetime import date
from datetime import timedelta
from datetime import datetime
from datetime import time
from datetime import date
import calendar
import time

class RegulateMeds:

    
    def __init__(self,daysOfWeek,timeOfDay,nameOfDrug):

        self.daysOfWeek=daysOfWeek
        self.timeOfDay=timeOfDay
        self.nameOfDrug=nameOfDrug

    
    
    #while self.userApproves==true:


    
    def intersection(self,lst1,lst2):
        lst3=[value for value in lst1 if value in lst2]
        return lst3

    def createSchedule(self):
        schedule={}
        x=self.daysOfWeek.lower().replace(" ","").split(",")
        print(x)
        days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        
        pillDays=self.intersection(x,days)

        key = pillDays

        value = self.storeTime()

        for x in range(len(key)):
            schedule[key[x]]=value  

        helperStr = ""
        
        for x,y in schedule.items():
            helperStr += str(x) + " at " + str(y) + "\n"
        
        prompt = "We will remind you to take " + self.nameOfDrug + " on: \n" + helperStr #json this and send to user
        #print(prompt)
        self.dateCheck(pillDays,self.storeTime())
        return prompt
        

    def storeTime(self):

        medTime=self.timeOfDay.lower().replace(" ","").split(",")
        medTime.sort()
        
        return medTime

##    def dateCheck(self,pillDays, medTime):
##
##        myDate=date.today()
##        strings = time.strftime("%H,%M")
##        t = strings.split(',')
##        numbers = [ int(x) for x in t ]
##        myHour = str(numbers[0])
##        myMin = str(numbers[1])
##        myTime = myHour +":"+myMin
##        myDate= calendar.day_name[myDate.weekday()]  
##
##        
##
##        for x in pillDays:
##            if x==myDate and myTime==medTime:
##                alertBool=True
##                #pass through as jason
##                alertBool = False
##                                
##        
    
    



#else: 

    
##meds = RegulateMeds(" Monday, Tuesday,Wednesday ,   SaturdAy",r"09:00,05:00,14:00","Advil")
##meds.createSchedule()

