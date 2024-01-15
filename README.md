# Weather-Data-API

**Purpose** 

Using a weather data services site, Visual Crossing, We needed to call the API in the code, retrieve the 15-day forecast for one location, and then going through each row in the data we needed to print a message to the user for the following weather conditions:

•	Check if the UV index will be 7 or higher

•	Check if rain is likely

•	Warn for freezing temperatures 

•	Warn users if temperature will be high (80 degrees Fahrenheit or above).

To accomplish this, I will be using mainly Python with some packages called pandas, csv, datetime, requests and matplotlib.pyplot. 

**Part A**

The two cities that will be compared will be Tokyo, Japan and Oslo, Norway. Personally, I've always loved these two cities and wish to visit them one day so I want to know what the weather will be like when I decide to travel there. The weather for these two countries currently are opposites as Tokyo is experiencing weather between the 60s and 70s whereas Oslo is experiencing weather in the 30s-to-40s-degree range until recently it barely hit 60 degrees Fahrenheit. Here are the plots for the linear graph and bar graph respectively.

![image](https://github.com/GucciRemyBoi/Weather-Data-API/assets/40637569/03fb981e-12b1-418e-af2e-7fe7ecacbff4)

I also showed on a bargraph the amount of rainfall that each city is experincing using pyplot as well (in inches)

![image](https://github.com/GucciRemyBoi/Weather-Data-API/assets/40637569/9f5a44a1-2b3a-4357-bdc3-d93e507cc3c9)

The data I stemmed these off were precipitation, or in the data file provided by Visual Crossing “precip” for the bar graphs and the “tempmin” and “tempmax” categories for the line graph. With part A, I did not provide any recommendation messages, but with the graphs it can show how the weather steadily changes throughout the year if we increase the data range from a month out to a year out. If I had to do this code again, I would like to implement a better run time as the graphs for part A take longer to open than it should have.

**Part B** 

In part B, I decided to choose a different city from Tokyo and Oslo and picked Berlin, Germany as my final one. Berlin is also a city I would like to visit in the future, but I have priorities for Tokyo and Oslo above it. In addition, Berlin is a balance between Tokyo and Oslo temperatures sitting between 40–60-degree Fahrenheit ranges. Here is the screenshot of my output for this:

![image](https://github.com/GucciRemyBoi/Weather-Data-API/assets/40637569/af49d399-d94b-49a8-ba1e-c85d7b4fd56c)

On a side note, for some reason the output included the time stamps 00:00:00 for only UV exposure which I thought was interesting and after looking at the file it turns out that Visual Crossing includes this in their data. Moving on, my recommendation messages included the date on a Year-Month-Data structure. Then I provided the data behind that date whether it was UV, freezing temps, or raining. Unfortunately, in Berlin there looked to be no forecast of rain within the next 15 days so I could not use that output message. With my output messages, I gave the users the information on how to combat such weathers and precautions behind them. This is extremely helpful as speaking for myself I did not know how damaging UV rays can be in general. This gave me great insight on how UV works and if it helps me understand how UV works, then thousands of other people out there could learn this information as well with output messages like these.

**Improvement** 

In the future, I would like to create more interactive graphs that show rainfall, snowfall, daily max and min temperatures, and display this on a website that shows the daily weather between these two cities in case there's anyone else out there that would love to travel to Oslo, Norway and Tokyo, Japan. In addition, I would also find ways to make my code work more smoothly as I said previous that some of the graphs took some time to display. 
