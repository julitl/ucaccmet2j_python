#.1

#1. Seattle,WA,GHCND:US1WAKG0038 => found this manually in the stations.csv

#2. 
# Firstly, importing json, so I can save this as a .json file later
import json 

# Importing csv as well, so the file stations.csv can be opened
import csv

# Opening the file
with open('precipitation.json') as file:
    precipitation = json.load(file)

# Read csv file to a list of dictionaries
with open('stations.csv') as file:
    stations = list(csv.DictReader(file))

# Making a dictionary to store results for each location
output_data1 = {}

# Loop through each station
for station in stations:
    # Extract the station code
    station_code = station['Station']
    location_name = station['Location']

# To check whether it is printing the correct output
print(stations)
