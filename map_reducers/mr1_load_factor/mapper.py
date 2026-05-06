#!/usr/bin/env python

import sys
import json

# Print to stdout in tabulation format
# station_id    timestamp  load_factor  status_valide
for line in sys.stdin:
    line = line.removeprefix("\ufeff")  # Windows pipe adds Utf8 BOM
        
    station = json.loads(line.strip())
    
    station_id = f'{station["contractName"]}_{station["number"]}'
    
    timestamp = station["lastUpdate"]
    
    available_bikes = station["totalStands"]["availabilities"]["bikes"]
    available_stands = station["totalStands"]["availabilities"]["stands"]
    capacity = available_bikes + available_stands
    load_factor = -1
    if capacity != 0:
        load_factor = available_bikes / capacity
    
    status = station["status"]
    status_valide = 1 if status == "OPEN" else 0
    
    print("\t".join([station_id, timestamp, str(load_factor), str(status_valide)]))
    
    