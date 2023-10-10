import requests
import os

# set your api key in your environment variable
api_key = os.environ.get("OWM_API_KEY")
if api_key is None:
    api_key = "set your api key"
    print("You need to set your api key in your environment variable.")

LATITUDE = 37.566536
LONGITUDE = 126.977966


def openweather(lat, lng, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"lat": lat,
                  "lon": lng,
                  "appid": api_key}
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    return response.json()


data = openweather(LATITUDE, LONGITUDE, api_key)
# print(data)

will_rain = False
print(data["weather"][0]["id"])
if int(data["weather"][0]["id"]) < 700:
    print("You need an umbrella.")
    will_rain = True
