import urllib.request
import json
import os 
import time

city = "nantes"
api_key = os.environ["JCDECAUX_API_KEY"]
filepath = "./files_to_add/" # executed from project root (..)

dynamic_url = f"https://api.jcdecaux.com/vls/v3/stations?contract={city}&apiKey={api_key}"
res = urllib.request.urlopen(dynamic_url)
data = json.loads(res.read().decode("utf-8"))

timestamp = int(time.time())
filename = f"{filepath}/{timestamp}.txt"
with open(filename, "x", encoding="utf-8") as f:
    for json_object in data:
        f.write(json.dumps(json_object)+"\n")