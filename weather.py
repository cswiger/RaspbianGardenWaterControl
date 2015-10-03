from urllib.request import urlopen
from json import loads
import ssl

api_key = "e366469ed8d5bd01b9d4a6cb8ed489ae"
lat = "38.353664"
long = "-81.687318"

def weather():
   url = urlopen("https://api.forecast.io/forecast/" + api_key + "/" + lat + "," + long)
   fc = url.read().decode('utf-8')
   url.close()
   jfc = loads(fc)

   return jfc
