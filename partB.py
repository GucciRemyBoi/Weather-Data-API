# Purpose: To use real time API to get weather information from Visual Crossing and print messages for harmful weather
# Author: Lorenz Wilkins
# Resources: Microsoft Word, Geeks for Geeks, Python Library, YouTube
# Date Modified: April 23rd, 2023

# Importing packages
import requests
import csv
from datetime import datetime, timedelta

# Setting up API and Parameters
url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Berlin%2C%20Germany?unitGroup=us&include=days&key=B2AKK4KYJXZFQXN96T2GMW29D&contentType=csv"
params = {
    "unitGroup": "US",
    "include": "days",
    "key": "B2AKK4KYJXZFQXN96T2GMW29D",
    "contentType": "csv"
}

# Make call to API and get response
response = requests.get(url, params = params)

# Retrieve the data from response
data = csv.DictReader(response.text.strip().split("\n"))

# Defining limits for uv, max temp, min temp and rain chances
uv_Limit = 7
rain_Chances = 0.1
cold_Limit = 40
hot_Limit = 80

# Go through data rows and print appropriate message
for row in data:
    # Convert data string to datetime object
    date_Str = row["datetime"]
    date = datetime.strptime(date_Str, "%Y-%m-%d")

    # Check for uv
    if float(row["uvindex"]) >= uv_Limit:
        print(f"On {date}, UV exposure is {row['uvindex']}. This is considered high and you should wear sunblock, wear UV sunglasses, and try to stay indoors.")
    
    # Check for rainfall chance
    if float(row["precip"]) >= rain_Chances:
        print(f"On {date}, there is a {row['precip']}% chance of rainfall. Bring an umbrella or rain coat.")

    # Check for cold temperatures
    if float(row["tempmin"]) <= cold_Limit:
        print(f"On {date_Str}, the temperature is {row['tempmin']} degrees, which is cold. Bring gloves, a coat, and stay indoors if possible.")
    
    # Check for hot temperatures
    if float(row["tempmax"]) >= hot_Limit:
        print(f"On {date_Str}, the temperature is {row['tempmax']} degrees, which is hot. Stay hydrated and avoid the sun if possible.")