import os
import urllib.request
import json


# Documentation de l'api: https://developer.jcdecaux.com/#/opendata/vls?page=getstarted

city = "nantes"
api_key = os.environ["JCDECAUX_API_KEY"]

print("------------------- STATIC DATA")
# static_url = f"https://developer.jcdecaux.com/rest/vls/stations/{city}.json"
# res = urllib.request.urlopen(static_url)
# print(res.url, res.status)
# data = json.loads(res.read())
# print(json.dumps(data, indent=True))

print("------------------- DYNAMIC DATA")
dynamic_url = f"https://api.jcdecaux.com/vls/v3/stations?contract={city}&apiKey={api_key}"
res = urllib.request.urlopen(dynamic_url)
print(res.url, res.status)
data = json.loads(res.read().decode("utf-8"))
print(json.dumps(data, indent=True))

