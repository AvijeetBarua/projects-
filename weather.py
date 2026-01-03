import json
import requests 
import sys 
if len(sys.argv) ==1:
    sys.exit("No city name was given")
try:
    n = sys.argv[1] .title()
except ValueError:
    sys.exit("Invalid city name")
try:
    response = requests.get(f"https://wttr.in/{n}?format=j1")
    weather_info  = response.json()
    current = weather_info["current_condition"][0]["temp_C"]
    print(f"The current temperature in {n} is {current}°C")
except requests.RequestException:
    pass 
