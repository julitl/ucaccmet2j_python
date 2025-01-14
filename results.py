#.1

#1. Seattle,WA,GHCND:US1WAKG0038

#2.
import json 
with open('precipitation.json') as file:
    precipitation = json.load(file)

seattle_rain_measurements = []

cincinnati_station_code = "GHCND:US1WAKG0038"

for measurement in precipitation:
    if measurement['station'] == cincinnati_station_code:
        seattle_rain_measurements.append(measurement)

print(seattle_rain_measurements) 

total_monthly_precipitation = {}
total_prec = 0

for measurement in seattle_rain_measurements:
    months = int(measurement['date'].split('-')[1])
    precipitation1 = measurement['value']
    if months in total_monthly_precipitation:
        total_monthly_precipitation[months] += precipitation1
    else:
        total_monthly_precipitation[months] = precipitation1

print(total_monthly_precipitation)

with open('results.json', 'w', encoding = 'utf-8') as file:
    json.dump(total_monthly_precipitation, file)

