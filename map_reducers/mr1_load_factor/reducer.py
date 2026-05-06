#!/usr/bin/env python

import sys

load_factor_by_station_id: dict[str, list[float]]= {}

for line in sys.stdin:
    line = line.removeprefix("\ufeff")  # Windows pipe adds Utf8 BOM
    
    [station_id, timestamp, load_factor, status] = line.strip().split("\t")
    
    if status == "1":
        if station_id not in load_factor_by_station_id:
            load_factor_by_station_id[station_id] = []

        load_factor_by_station_id[station_id].append(float(load_factor))
   
        
for station, load_factors in load_factor_by_station_id.items():
    print("\t".join([station, str(sum(load_factors) / len(load_factors))]))
