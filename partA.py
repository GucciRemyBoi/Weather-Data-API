# Purpose: To create a plot point for max temp for two cities, then rainfall for the two cities
# Author: Lorenz Wilkins
# Resources: Microsoft Word, Geeks for Geeks, Python plotlib library, Pandas
# Date Modified: April 22nd, 2023

# Importing Packages
import pandas as pd # Panda is a python library for data manipulation and analysis, able to write in csv as well.
import matplotlib.pyplot as plt

# Using panda to read the weather file
weather = pd.read_csv("Weather.csv")

# Convert datetime column to pandas datetime
weather["datetime"] = pd.to_datetime(weather["datetime"])

# Filtering data to Oslo, Norway
weather_Oslo = weather[weather["name"] == "Oslo, Norway"]
temp_Oslo = weather_Oslo["temp"]

# Filtering data to Tokyo, Japan
weather_Tokyo = weather[weather["name"] == "Tokyo, Japan"]
temp_Tokyo = weather_Tokyo["temp"]

# Getting max temp for each location
max_Temp_Oslo = weather_Oslo.groupby(pd.Grouper(key="datetime", freq="D"))["tempmax"].max()
max_Temp_Tokyo = weather_Tokyo.groupby(pd.Grouper(key="datetime", freq="D"))["tempmax"].max()

# Creating line chart for daily max temp for Oslo and Tokyo
fig, ax = plt.subplots()
max_Temp_Oslo.plot(ax=ax, label = "Oslo, Norway")
max_Temp_Tokyo.plot(ax=ax, label = "Tokyo, Japan")
plt.title("Daily Max Temperature for Tokyo and Oslo")
plt.xlabel("Date")
plt.ylabel("Temperature (°F)") # Note: Don't ask me how I was able to do "°", This took me the longest time and I'd strongly like not to revisit it
ax.set_ylim([min(temp_Oslo.min(), temp_Tokyo.min()), max(max_Temp_Oslo.max(), max_Temp_Tokyo.max())])
plt.legend()
plt.show()

# Extracting total rainfall
rainfall_Oslo = weather_Oslo['precip'].sum()
rainfall_Tokyo = weather_Tokyo['precip'].sum()

# Creating bar graph for rainfall
fig, ax = plt.subplots()
ax.bar(["Oslo, Norway", "Tokyo, Japan"], [rainfall_Oslo, rainfall_Tokyo])
plt.title("Rainfall for Oslo and Tokyo")
plt.xlabel("Cities")
plt.ylabel("Rainfall (inches)")
plt.show()