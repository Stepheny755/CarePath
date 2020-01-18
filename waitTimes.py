import requests,json
from xml.dom import minidom

class waitTimes():

    uri = 'http://hqontario.ca/webservices/wsWaitTimes.asmx/getTableDataAllHospitals'

    def __init__(self):
        pass


    def getWaitTimeTable(self):
        payload={'language':'en-CA'}
        table = requests.post(self.uri,payload);
        xmlDocument = minidom.parseString(table.text)
        itemList = xmlDocument.getElementsByTagName('string')
        dataList = itemList[0].firstChild.nodeValue
        for value in json.loads(dataList):
            print(value)


if(__name__=="__main__"):
    w=waitTimes()
    w.getWaitTimeTable()
    #w.testRequest()
