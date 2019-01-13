import sys
import requests
import json


loc = None
if len(sys.argv) == 1:
    loc = raw_input("Where are you? ")
elif len(sys.argv) == 2:
    loc = sys.argv[1]
else:
    print("Please run script with the command \'python weather.py\' or \'python weather.py <location>\'")

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + loc + "&APPID=0124b9ecc3f7e62e522eca1c30afbc30")
temp = response.json()["main"]["temp"]
print("Chicago weather:\n" + temp + " degrees Fahreneheit")