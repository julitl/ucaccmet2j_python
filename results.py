#.1

#1. Seattle,WA,GHCND:US1WAKG0038 => found this manually in the stations.csv

#2. 
# Firstly, importing json, so I can save this as a .json file later
import json 

#3.

# Importing csv as well, so the file stations.csv can be opened
import csv

# Opening the file
with open('precipitation.json') as file:
    precipitation = json.load(file)

# Read csv file to a list of dictionaries
with open('stations.csv') as file:
    stations = list(csv.DictReader(file))

# Opening the file
with open('precipitation.json') as file:
    precipitation = json.load(file)

# Making a list called seattle_rain_measirements
seattle_rain_measurements = []

# Defining the station code, as we are looking at Settle only
seattle_station_code = "GHCND:US1WAKG0038"

# Loop for measurements data & append for Seattle 
for measurement in precipitation:
    if measurement['station'] == seattle_station_code:
        seattle_rain_measurements.append(measurement)

# Print seattle_rain_measurments to check 
print(seattle_rain_measurements) 

# Making a dictionary for total_monthly_precipitation
total_monthly_precipitation = {}

# Loop for the list seattle_rain_measurements
for measurement in seattle_rain_measurements:
    # Extract the month from the date
    months = int(measurement['date'].split('-')[1])
    # Get the precipitation value for this measurement
    precipitation1 = measurement['value']
    # Check if the month is already in the dictionary
    if months in total_monthly_precipitation:
        # If month exists, add the precipitation to the existing total
        total_monthly_precipitation[months] += precipitation1
        # If month does not exist, add a new entry for that month
    else:
        total_monthly_precipitation[months] = precipitation1

# Print the total monthly precipitation 
print(total_monthly_precipitation)

# Save the result to a JSON file called 'results.json'
with open('results.json', 'w', encoding = 'utf-8') as file:
    json.dump(total_monthly_precipitation, file)

#.2

#1.

# New variable for yearly percipitation for Seattle
yearly_per_seattle = 0

# Loop through each measurement in the rain data
for measurement in seattle_rain_measurements:
    # Add the precipitation value to the yearly total
    yearly_per_seattle += measurement['value']

# Print the total yearly precipitation
print(yearly_per_seattle)

#2.

# Making a dictionary for the relative precipitation per month
relative_monthly_precipitation = {}

key = 1
# Loop for each measurement in the dictionary total monthly precipitation
for measurement in total_monthly_precipitation:
    # Adding in the 1st spot of the new dictionary the total monthly precipitation divided by the yearly percipitation
    relative_monthly_precipitation[key] =  total_monthly_precipitation[key]/ yearly_per_seattle
    key += 1

# Print the relative monthly precipitation 
print(relative_monthly_precipitation)

# Summary data saved into .json file
output_data = {'Monthly Precipitation': total_monthly_precipitation, 'Yearly Precipitation': yearly_per_seattle, 'Relative Monthly Precipitation': relative_monthly_precipitation}
with open('results.json', 'w', encoding = 'utf-8') as file:
    json.dump(output_data, file)