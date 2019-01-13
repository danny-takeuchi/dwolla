import sys
import requests


loc = None
if len(sys.argv) == 1:
    loc = input("Where are you? ")
elif len(sys.argv) == 2:
    loc = sys.argv[1]
else:
    print("Please run script with the command \'python weather.py\' or \'python weather.py <location>\'")

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + loc + "&APPID=0124b9ecc3f7e62e522eca1c30afbc30&units=imperial")
obj = response.json()
code = obj["cod"]
if code == "404":
    print("City not found")
else:
    tempF = round(obj["main"]["temp"])
    print(loc + " weather:\n" + str(tempF) + " degrees Fahreneheit")