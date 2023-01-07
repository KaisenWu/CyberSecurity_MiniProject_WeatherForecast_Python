#!/usr/bin/python

# Import required library.
import json, requests
from geopy.geocoders import Nominatim
from datetime import datetime, timezone

# Build the banner function.
def showBanner():
    print("CyberSecurity MiniProject: Weather Forecast")
    print("Created by Kaisen Wu")

# Build function to print menu.
def printMenu(optionDict):
    print("Please select one of following options:")
    for key in optionDict.keys():
        print("{}: {}".format(key, optionDict[key]))

# Build the option1 function.
def option1():
    # Create a loc object.
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("Douglas College (New Westminster)")
    # Get latitute and lonitude.
    lat = getLoc.latitude
    long = getLoc.longitude
    # Construct a url.
    url = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&hourly=temperature_2m,precipitation".format(lat,long)
    # Grab json data.
    response = requests.get(url)
    # Store the json as a string.
    jsonStr = response.text
    # Convert json string to a dictionary.
    jsonDict = json.loads(jsonStr)
    # Convert the dictionary to formated json string.
    niceJson = json.dumps(jsonDict,indent=4)
    # Save the json output data.
    with open('weather_forecast_output.json','w') as jsonfile:
        jsonfile.write(niceJson)

# Build the option2 function.
def option2():
    while(True):
        # Initial the latitute and longitude variables/
        lat = 100
        long = 2000
        # Prompt user to input.
        try:
            lat = float(input('Input latitude >>'))
            long = float(input('Input longitude >>'))
        # Define exception.   
        except:
            print("Please input number.")

        if lat > -90 and lat < 90 and long > -180 and long < 180:
            # Construct a url.
            url = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&hourly=temperature_2m".format(lat,long)
            # Grab json data.
            response = requests.get(url)
            # Store the json as a string.
            jsonStr = response.text
            # Convert json string to a dictionary.
            jsonDict = json.loads(jsonStr)
            # Store the time to a list.
            timeList = jsonDict.get("hourly").get("time")
            # Store all temprature values to a list.
            tempList = jsonDict.get("hourly").get("temperature_2m")
            # Get the current utc time.
            currentUtcDate = datetime.now(timezone.utc).isoformat()[:12]
            # Store the current hour index.
            for i,v in enumerate(timeList):
                if v[:12] == currentUtcDate:
                    currentIndex = i
                    break
            # Creat the 6 hour index list.
            indexList = []
            for i in range(currentIndex+1,currentIndex+7):
                indexList.append(i)
            # Print the next 6 hour temprature.
            for i,index in enumerate(indexList):
                print("The next {} hour temperature is: {}".format(i+1,tempList[index]))
            exit()
        else:
            print("Invalid longitude or latitude.")