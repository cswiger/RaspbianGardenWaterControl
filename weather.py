from urllib.request import urlopen
from json import loads
import ssl

api_key = "your forecast.io api key here"
lat = "37.8267"
long = "-122.423"

def weather():
   url = urlopen("https://api.forecast.io/forecast/" + api_key + "/" + lat + "," + long)
   fc = url.read().decode('utf-8')
   url.close()
   jfc = loads(fc)

   return jfc
