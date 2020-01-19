import requests,json,googlemaps,math

class Map():

    apikey = ''
    gmaps = ''


    def __init__(self):
        self.apikey = open('keys/gcloud.txt',"r").read().strip()
        self.gmaps = googlemaps.Client(key=self.apikey)

    def getGeoCode(self,locationQuery):
        geocodeResult = self.gmaps.geocode(str(locationQuery))
        return(geocodeResult[0]['geometry']['location']['lat'],geocodeResult[0]['geometry']['location']['lng'])

    def getAddress(self,coordx,coordy):
        reverseResult = self.gmaps.reverse_geocode((coordx,coordy))
        return reverseResult

    def findPlaces(self,inputQuery,locationBias=None,radius=None):
        searchResult = self.gmaps.places(inputQuery,location=locationBias,radius=radius)
        return searchResult['results']

    def parsePlace(self,searchResult):
        searchResult = searchResult['results']
        for val in searchResult:
            print(val)
            print()

    def getDistanceTime(self,orig,dest):
        dirs = self.gmaps.directions(orig,dest)[0]['legs'][0]['duration']['value']
        return dirs

if(__name__=="__main__"):
    m = Map()
    c=m.findPlace("yang's tea",m.getGeoCode("89 Chestnut Street"),0.01)
    m.parsePlace(c)
    #print(c)
