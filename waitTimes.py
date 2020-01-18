import requests,json,csv,os
from xml.dom import minidom

class waitTimes():

    uri = 'http://hqontario.ca/webservices/wsWaitTimes.asmx/getTableDataAllHospitals'

    def __init__(self):
        self.waitTimeList = []

    def readWaitTimes(self):
        readList = []
        filename="waittimes.csv"
        path="resources"
        with open(os.path.join(path,filename).strip(),'r') as r:
            readList = list(csv.reader(r,delimiter=','))
        self.waitTimeList = readList
        return readList

    def getHospitalWaitTime(self,name):
        if not self.waitTimeList:
            self.readWaitTimes()
        for i in self.waitTimeList:
            if(name==i[0]):
                return i[1]

    def getHospitalList(self):
        payload={'language':'en-CA'}
        table = requests.post(self.uri,payload);
        xmlDocument = minidom.parseString(table.text)
        itemList = xmlDocument.getElementsByTagName('string')
        dataList = itemList[0].firstChild.nodeValue
        return json.loads(dataList)

    def parseHospitalList(self,hospitalList):
        for i in hospitalList:
            print(i)

if(__name__=="__main__"):
    w=waitTimes()
    d=w.getHospitalList()
    w.parseHospitalList(d)
    w.getHospitalWaitTime("Sensenbrenner Hospital")
    #w.testRequest()
